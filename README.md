# Benefit Audit Intelligence: Algorithmic Governance & GRC Framework

![Executive Dashboard](https://raw.githubusercontent.com/deckSnover/benefit-audit-intelligence/main/data/output/executive_dashboard_grc_47k.png)

## 📌 Visão Geral e Resumo Executivo
O RH pode estar a gerar prejuízo financeiro mesmo quando o processo administrativo está "correto". Este projeto apresenta um framework de **Auditoria Algorítmica** desenvolvido para solucionar o *Financial Leakage* (vazamento de caixa) em faturas de benefícios de alta volumetria (faturas acima de R$ 2MM/mês).

### O Problema: O "Gap" Operacional
Existe um delay sistémico entre operadoras de saúde e a realidade do RH. Este delay gera cobranças indevidas de vidas inativas que são invisíveis à conferência manual em faturas complexas.

## 🛠️ Stack Técnica e Metodologia
* **Linguagem:** Python 3.12+.
* **Data Engine:** Pandas & NumPy para Data Matching e ETL de alta performance.
* **Visualização:** Seaborn & Matplotlib (Estilo de Relatório Executivo de Alto Contraste).
* **Framework:** GRC Intelligence (Arquitetura Híbrida Proprietária).

## 🚀 Funcionalidades Chave
1. **Automated Data Matching:** Cruzamento escalável entre faturas (.csv/txt) e a base real de colaboradores do ERP (Protheus, Senior, SAP).
2. **Risk Density Distribution:** Utilização de *Kernel Density Estimation* (KDE) para isolar estatisticamente o comportamento de custos de vidas em compliance versus anomalias financeiras.
3. **Pre-payment Audit:** Detecção de inconformidades antes da liquidação financeira, protegendo o caixa imediatamente.

## 📈 Resultados Demonstrados (Cenário Corporativo)
No modelo de simulação de alta fidelidade incluído:
* **Base Total Auditada:** R$ 2.410.254,00.
* **Recovery Potential (Vazamento):** R$ 358.122,00 (14.85% de economia identificada).
* **Status:** Identificação de falha sistémica da operadora, protegendo o EBITDA da companhia.

---
**Nota de Propriedade Intelectual:** O core engine de integração com bancos de dados de produção (SQL/ERP) e as regras de negócio específicas são **proprietários**. Este repositório contém a camada de inteligência visual e o simulador de auditoria para fins de demonstração de metodologia.

**Autor:** Igor Hilario Silva  
**Área de Atuação:** GRC & Data Intelligence | People Analytics
