# Benefit Audit Intelligence: Algorithmic Governance & GRC Framework

![Executive Dashboard](reports/executive_dashboard_grc_47k.png)

## 📌 Vision & Executive Summary
O RH pode estar gerando prejuízo mesmo quando o processo administrativo está "correto". Este projeto demonstra um framework de **Auditoria Algorítmica** desenvolvido para solucionar o *Financial Leakage* (vazamento de caixa) em faturas de benefícios de alta volumetria.

### O Problema: O "Gap" Operacional
Mesmo com o cumprimento rigoroso dos ritos de exclusão, bloqueio de cartões e atualização de ERP, existe um delay sistêmico entre operadoras de saúde e a realidade do RH. Este delay gera cobranças indevidas de vidas inativas que são invisíveis à conferência manual.

## 🛠️ Tech Stack & Methodology
* **Language:** Python 3.14+
* **Data Engine:** Pandas & NumPy para Data Matching.
* **Visualization:** Seaborn & Matplotlib (Executive Reporting Style).
* **Framework:** GRC Intelligence (Proprietary).

## 🚀 Key Features
1. **Automated Data Matching:** Cruzamento entre faturas (.csv/txt) e a base real de colaboradores do ERP (Protheus/Senior/SAP).
2. **Risk Density Distribution:** Utilização de *Kernel Density Estimation* (KDE) para identificar anomalias em tickets médios de inativos.
3. **Pre-payment Audit:** Detecção de inconformidades antes da liquidação financeira, eliminando a necessidade de processos reativos de reembolso.

## 📈 Resultados Demonstrados
No modelo de simulação incluído:
* **Base Auditada:** R$ 393.994,00
* **Recovery Potential (Vazamento):** R$ 96.522,00 (24.50%)
* **Status:** Identificação de falha sistêmica da operadora, sem erro operacional do RH.

---
**Nota de Propriedade Intelectual:** O core engine de integração com bancos de dados de produção (SQL/ERP) e as regras de negócio específicas são protegidos. Este repositório contém a camada de inteligência visual e o simulador de auditoria para fins de demonstração de metodologia.

**Author:** Igor Hilario Silva  
**Field:** GRC & Data Intelligence | People Analytics