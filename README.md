# FarmTech Solutions - Projeto Completo CAP1

Este repositório contém o projeto completo do FarmTech Solutions, desenvolvido para a disciplina CAP1. O projeto é composto por duas entregas principais focadas em Machine Learning e Computação em Nuvem.

## 📋 Estrutura do Projeto

### 📊 Entrega 1: Machine Learning
**Localização:** `FarmTech_Fase5_Entrega1/`

- **Objetivo:** Análise exploratória de dados (EDA), clusterização, detecção de outliers e desenvolvimento de modelos de regressão para predição de rendimento agrícola
- **Principais recursos:**
  - Notebook Jupyter completo com análise exploratória
  - Implementação de PCA e algoritmos de clusterização (KMeans, DBSCAN)
  - Detecção de outliers usando IQR e Isolation Forest
  - 5 modelos de regressão: Linear, Ridge, Random Forest, Gradient Boosting, KNN
  - Pipeline completo com validação e comparação de métricas
  - Exportação automática do melhor modelo

### ☁️ Entrega 2: Computação em Nuvem
**Localização:** `FarmTech_Fase5_Entrega2_Cloud/`

- **Objetivo:** API FastAPI para deploy em nuvem com predição de rendimento agrícola
- **Principais recursos:**
  - API REST completa com FastAPI
  - Carregamento automático do modelo da Entrega 1
  - Treinamento automático se modelo não existir
  - Containerização com Docker
  - Testes automatizados
  - Documentação automática com Swagger/OpenAPI

## 🚀 Como Usar

### Pré-requisitos
- Python 3.8+
- pip
- Docker (opcional, para a Entrega 2)

### Entrega 1 - Machine Learning
```bash
cd FarmTech_Fase5_Entrega1/
# Se tiver o arquivo crop_yield.csv, coloque em data/
# Abra e execute o notebook: notebooks/FarmTech_Entrega1.ipynb
```

### Entrega 2 - API em Nuvem

#### Execução Local
```bash
cd FarmTech_Fase5_Entrega2_Cloud/
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Acesse: http://127.0.0.1:8000/docs

#### Execução com Docker
```bash
cd FarmTech_Fase5_Entrega2_Cloud/
docker build -t farmtech-yield-api .
docker run -it --rm -p 8000:8000 --name farmtech-api farmtech-yield-api
```

## 📝 Exemplo de Uso da API

```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d @sample_request.json
```

## 🔧 Funcionalidades Principais

### Machine Learning (Entrega 1)
- ✅ Análise exploratória completa dos dados
- ✅ Implementação de PCA para redução de dimensionalidade
- ✅ Clusterização com KMeans e DBSCAN
- ✅ Detecção de outliers (IQR + Isolation Forest)
- ✅ 5 modelos de regressão com validação cruzada
- ✅ Pipeline automatizado de treinamento
- ✅ Exportação de métricas e predições
- ✅ Visualizações usando matplotlib

### API Cloud (Entrega 2)
- ✅ API REST com FastAPI
- ✅ Endpoints para predição e status
- ✅ Carregamento automático de modelo
- ✅ Treinamento fallback automático
- ✅ Validação de dados com Pydantic
- ✅ Containerização Docker
- ✅ Documentação automática
- ✅ Testes automatizados
- ✅ Pronto para deploy em nuvem

## 🌟 Diferenciais

- **Robustez:** Sistema funciona mesmo sem dados iniciais (gera dataset sintético)
- **Flexibilidade:** API se adapta automaticamente aos modelos disponíveis
- **Deploy Ready:** Configurado para principais provedores cloud (Render, Railway, Fly.io)
- **Documentação:** READMEs detalhados e código bem documentado
- **Testes:** Cobertura de testes para garantir qualidade

## 📁 Estrutura de Arquivos

```
.
├── FarmTech_Fase5_Entrega1/
│   ├── notebooks/
│   │   └── FarmTech_Entrega1.ipynb
│   ├── data/                     # Dados de entrada
│   ├── models/                   # Modelos treinados
│   ├── artifacts/               # Métricas e predições
│   └── README.md
├── FarmTech_Fase5_Entrega2_Cloud/
│   ├── app/
│   │   ├── main.py              # Aplicação FastAPI
│   │   ├── model.py             # Lógica do modelo
│   │   └── schemas.py           # Esquemas Pydantic
│   ├── tests/
│   │   └── test_api.py          # Testes automatizados
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── sample_request.json
│   └── README.md
└── instrucoes.txt               # Instruções originais

```

## 🏆 Status dos Requisitos

- [x] **Entrega 1:** Notebook completo com EDA, ML e exportação
- [x] **Entrega 2:** API FastAPI containerizada e testada
- [x] **Integração:** API compatível com modelos da Entrega 1
- [x] **Deploy:** Pronto para deploy em qualquer provedor cloud
- [x] **Documentação:** READMEs detalhados e código documentado

## 📞 Suporte

Para dúvidas ou problemas, consulte os READMEs específicos de cada entrega ou as instruções detalhadas no arquivo `instrucoes.txt`.

---

**Desenvolvido para:** Disciplina CAP1  
**Foco:** Machine Learning e Computação em Nuvem  
**Tecnologias:** Python, FastAPI, Docker, scikit-learn, pandas, matplotlib
