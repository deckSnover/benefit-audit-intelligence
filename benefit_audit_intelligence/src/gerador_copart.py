import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def gerar_dashboard_hibrido_grc():
    # Simulação de alta densidade
    np.random.seed(42)
    valor_ativo = np.random.normal(loc=350, scale=120, size=850) 
    valor_inativo = np.random.normal(loc=650, scale=180, size=150) 
    
    df = pd.DataFrame({
        'Valor': np.concatenate([valor_ativo, valor_inativo]),
        'Status': ['ATIVO'] * 850 + ['INATIVO'] * 150
    })

    plt.style.use('dark_background')
    fig, ax = plt.subplots(1, 2, figsize=(18, 8), gridspec_kw={'width_ratios': [1.6, 1]})
    
    # Título Híbrido: Metodologia em Inglês | Contexto em Português
    fig.suptitle('EXECUTIVE AUDIT SUMMARY | Governança de Benefícios', 
                 fontsize=22, fontweight='bold', color='#FFFFFF', y=1.05)
    
    # --- GRÁFICO 1: Distribuição de Risco ---
    sns.kdeplot(data=df[df['Status'] == 'ATIVO'], x='Valor', fill=True, ax=ax[0], 
                color='#2E8B57', label='Compliance (Vidas Ativas)', alpha=0.5)
    sns.kdeplot(data=df[df['Status'] == 'INATIVO'], x='Valor', fill=True, ax=ax[0], 
                color='#BE123B', label='Financial Leakage (Inativos)', alpha=0.7)
    
    ax[0].set_title('RISK DENSITY | Distribuição de Ticket Médio', fontsize=15, loc='left', pad=15)
    ax[0].set_xlabel('Valor por Guia Audorada (R$)', fontsize=12)
    ax[0].legend(fontsize=11)

    # --- GRÁFICO 2: KPIs Executivos ---
    metrics = ['Base Total Auditada', 'Recovery Potential', 'Leakage Rate']
    values = [df['Valor'].sum(), df[df['Status']=='INATIVO']['Valor'].sum(), (df[df['Status']=='INATIVO']['Valor'].sum()/df['Valor'].sum())*100]
    colors = ['#4B5563', '#BE123B', '#F59E0B']
    
    bars = ax[1].barh(metrics, values, color=colors)
    ax[1].set_title('KEY PERFORMANCE INDICATORS | KPIs de Auditoria', fontsize=15, loc='left', pad=15)
    
    for i, bar in enumerate(bars):
        w = bar.get_width()
        txt = f'R$ {w:,.0f}' if i < 2 else f'{w:.2f}%'
        ax[1].text(w + (max(values) * 0.05), bar.get_y() + bar.get_height()/2, txt, va='center', fontweight='bold')

    ax[1].set_xlim(0, max(values) * 1.5)
    plt.tight_layout()
    plt.figtext(0.99, 0.01, 'Framework by Igor Hilario Silva | GRC & Data Intelligence', ha='right', alpha=0.6)
    
    plt.savefig('dashboard_final_hibrido.png', dpi=300, bbox_inches='tight')
    print("💎 Dashboard Híbrido gerado com sucesso!")

gerar_dashboard_hibrido_grc()