import pandas as pd
import os

# Garantir estrutura de pastas
os.makedirs('data/input', exist_ok=True)

def gerar_ecossistema_dados():
    # 1. Base de Funcionários (O que o RH tem no ERP)
    rh_data = {
        'matricula': [1001, 1002, 1003, 1004, 1005],
        'nome': ['Igor Hilario', 'Ana Silva', 'Marcos Oliveira', 'Luciana Costa', 'Ricardo Santos'],
        'status_erp': ['Ativo', 'Ativo', 'Inativo', 'Ativo', 'Inativo'],
        'valor_plano_correto': [450.00, 250.00, 0.00, 250.00, 0.00]
    }
    df_rh = pd.DataFrame(rh_data)
    df_rh.to_csv('data/input/base_rh_modelo.csv', index=False, sep=';')

    # 2. Base da Operadora (A Fatura com erros/vazamentos)
    # Injetando erros: Cobrança de inativos (1003 e 1005) e valores incorretos
    fatura_data = {
        'matricula': [1001, 1002, 1003, 1004, 1005],
        'valor_faturado': [450.00, 250.00, 450.00, 280.00, 450.00], # 1004 está com valor a maior
        'status_operadora': ['Ativo', 'Ativo', 'Ativo', 'Ativo', 'Ativo']
    }
    df_fatura = pd.DataFrame(fatura_data)
    df_fatura.to_csv('data/input/fatura_operadora_modelo.csv', index=False, sep=';')
    
    print("✅ Bases de RH e Fatura geradas com sucesso em /data/input/")

if __name__ == "__main__":
    gerar_ecossistema_dados()