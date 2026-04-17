import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def executar_auditoria():
    # 1. Carregar as bases criadas pelo setup_dados
    df_rh = pd.read_csv('data/input/base_rh_modelo.csv', sep=';')
    df_fatura = pd.read_csv('data/input/fatura_operadora_modelo.csv', sep=';')

    # 2. Cruzamento de Dados (Matching)
    df = pd.merge(df_fatura, df_rh, on='matricula', how='left')

    # 3. Lógica de Risco e Vazamento (Leakage)
    # Identifica cobrança de inativos ou valores acima do plano
    df['Vazamento'] = (df['status_erp'] == 'Inativo') | (df['valor_faturado'] > df['valor_plano_correto'])
    df['Valor_Recuperavel'] = df.apply(lambda x: x['valor_faturado'] if x['Vazamento'] else 0, axis=1)

    # 4. Gerar Dashboard Executivo
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Gráfico de barras mostrando o potencial de recuperação
    sns.barplot(x='nome', y='valor_faturado', data=df, hue='Vazamento', palette={True: '#BE123B', False: '#2E8B57'})
    
    plt.title('AUDITORIA DE BENEFÍCIOS: RECUPERAÇÃO DE CAIXA', fontsize=15, fontweight='bold')
    plt.ylabel('Valor da Fatura (R$)')
    plt.xlabel('Colaborador')
    
    # Salvar para o GitHub
    os.makedirs('data/output', exist_ok=True)
    plt.savefig('data/output/executive_dashboard_grc_47k.png', dpi=300, bbox_inches='tight')
    print(f"📊 Auditoria finalizada. Total recuperável: R$ {df['Valor_Recuperavel'].sum():.2f}")

if __name__ == "__main__":
    executar_auditoria()