# FarmTech Solutions — Fase 5 (Entrega 1: ML)

Este pacote contém:
- `notebooks/FarmTech_Entrega1.ipynb` — notebook completo com EDA, clusterização, 5 modelos de regressão e exportação do melhor modelo.
- `data/` — coloque aqui o arquivo **crop_yield.csv** (caso possua). Se ausente, um dataset sintético é gerado automaticamente.
- `models/` — melhor modelo salvo como `best_model.pkl`.
- `artifacts/` — métricas (`metrics.csv`) e predições (`predicoes_completas.csv`).
- `reports/` — espaço para relatórios.

## Como usar
1. Abra o notebook e execute todas as células.
2. Se tiver o arquivo oficial `crop_yield.csv`, salve-o em `data/` antes de rodar.
3. Ao final, confira `artifacts/metrics.csv` para comparar modelos e `models/best_model.pkl` para deploy.

> Observação: gráficos são feitos com **matplotlib** (sem seaborn) conforme solicitado.
