import pdfplumber
import os
import pandas as pd
import re

PASTA_ENTRADA = "data/input"
PASTA_SAIDA = "data/output"

def extrair_dados_unimed(caminho_pdf):
    extracao = []
    cod_titular_grupo = ""
    nome_titular_grupo = ""
    cnpj_identificado = "NÃO LOCALIZADO"

    with pdfplumber.open(caminho_pdf) as pdf:
        for pagina in pdf.pages:
            texto = pagina.extract_text()
            if not texto: continue
            
            linhas = texto.split('\n')
            for linha in linhas:
                # 1. BUSCA PELO CAMPO IDENTIFICADOR: CPF/CNPJ
                if "CPF/CNPJ:" in linha:
                    # Captura o número que vem após o campo CPF/CNPJ:
                    match_cnpj = re.search(r'CPF/CNPJ:\s+([\d\./-]+)', linha)
                    if match_cnpj:
                        cnpj_identificado = match_cnpj.group(1).strip()

                # 2. Identifica o Titular da seção para vincular os dependentes
                if "Titular:" in linha:
                    match_t = re.search(r'Titular:\s+(\d+)\s+(.*?)\s+Matrícula:', linha)
                    if match_t:
                        cod_titular_grupo = match_t.group(1).strip()
                        nome_titular_grupo = match_t.group(2).strip()

                # 3. Processa apenas as linhas reais de despesa (COPAR_BH ou COPAR INT)
                if "COPAR_" in linha or "COPAR INT" in linha:
                    partes = linha.split()
                    
                    # O Código do Usuário é a segunda parte. 
                    # Validamos se é um número para evitar linhas de texto sujas.
                    cod_usuario_linha = partes[1].replace('"', '') 
                    if not cod_usuario_linha.isdigit():
                        continue

                    # Localiza a data para isolar o nome do beneficiário
                    nome_beneficiario = ""
                    for i, parte in enumerate(partes):
                        if re.match(r'\d{2}/\d{2}/\d{4}', parte):
                            # O nome está entre o código e a data
                            nome_cru = " ".join(partes[2:i-1])
                            nome_beneficiario = re.sub(r'[^a-zA-Z\s]', '', nome_cru).strip()
                            break

                    # Captura o valor da coparticipação (penúltimo elemento)
                    try:
                        valor_raw = partes[-2].replace('"', '').replace('.', '').replace(',', '.')
                        valor_float = float(valor_raw)
                    except:
                        valor_float = 0.0

                    # CRITÉRIO DE CHAVE ÚNICA:
                    # Se o código da linha for igual ao titular da seção, classifica como Titular.
                    parentesco = "Titular" if cod_usuario_linha == cod_titular_grupo else "Dependente"
                    
                    extracao.append({
                        "CNPJ Unidade": cnpj_identificado,
                        "Titular do Grupo": nome_titular_grupo,
                        "Cód. Usuário": cod_usuario_linha,
                        "Beneficiário": nome_beneficiario,
                        "Tipo": parentesco,
                        "Valor Copart": valor_float
                    })
                    
    return extracao

def executar_auditoria():
    if not os.path.exists(PASTA_SAIDA):
        os.makedirs(PASTA_SAIDA)

    arquivos = [f for f in os.listdir(PASTA_ENTRADA) if f.endswith(".pdf")]
    consolidado = []

    for arq in arquivos:
        print(f"📄 Lendo campo CNPJ do arquivo: {arq}")
        caminho = os.path.join(PASTA_ENTRADA, arq)
        dados = extrair_dados_unimed(caminho)
        consolidado.extend(dados)

    if consolidado:
        df = pd.DataFrame(consolidado)
        caminho_xlsx = os.path.join(PASTA_SAIDA, "auditoria_consolidada_cnpj.xlsx")
        df.to_excel(caminho_xlsx, index=False)
        
        print(f"\n✅ Sucesso! {len(df)} registros processados.")
        print(f"💰 Valor Total Consolidado: R$ {df['Valor Copart'].sum():.2f}")
        print(f"📂 Arquivo salvo em: {caminho_xlsx}")
    else:
        print("⚠️ Nenhum dado localizado nos arquivos PDF.")

if __name__ == "__main__":
    executar_auditoria()