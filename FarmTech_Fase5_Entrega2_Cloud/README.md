
# FarmTech Solutions — Fase 5 (Entrega 2: Computação em Nuvem)

API **FastAPI** para previsão de **Rendimento (t/ha)** com base nas variáveis do projeto.
Compatível com o modelo salvo na Entrega 1 (`best_model.pkl`) — mas **se não houver modelo**, a API **treina automaticamente** (com `data/crop_yield.csv` se presente, ou com um dataset sintético).

## Estrutura
```
app/
  main.py            # Endpoints FastAPI
  model.py           # Carregamento/treino de modelo e pré-processamento
  schemas.py         # Esquemas Pydantic das requisições/respostas
requirements.txt
Dockerfile
```

## Como executar localmente (sem Docker)
1. Crie um virtualenv e instale dependências:
   ```bash
   pip install -r requirements.txt
   ```

2. (Opcional) Coloque `crop_yield.csv` em `data/` ou copie `models/best_model.pkl` gerado na Entrega 1 para `models/`.
3. Rode o servidor:
   ```bash
   uvicorn app.main:app --reload
   ```
4. Abra **http://127.0.0.1:8000/docs** para testar.

## Como executar com Docker
```bash
docker build -t farmtech-yield-api .
docker run -it --rm -p 8000:8000   -v $PWD/data:/app/data   -v $PWD/models:/app/models   --name farmtech-api farmtech-yield-api
```
> Monte volumes para que a API encontre `data/crop_yield.csv` ou `models/best_model.pkl`.

## Endpoints principais
- `GET /` — status, features e origem do modelo (`model_status`: `loaded_existing`, `trained_from_csv` ou `trained_synthetic`).
- `GET /health` — checagem simples.
- `POST /predict` — previsão. **Body (JSON) exemplo:**
```json
{
  "items": [
    {
      "Cultura": "Cultura_1",
      "Precipitação (mm dia 1)": 5.2,
      "Umidade específica a 2 metros (g/kg)": 7.8,
      "Umidade relativa a 2 metros (%)": 68.0,
      "Temperatura a 2 metros (ºC)": 24.3
    },
    {
      "Cultura": "Cultura_3",
      "Precipitação (mm dia 1)": 1.0,
      "Umidade específica a 2 metros (g/kg)": 5.1,
      "Umidade relativa a 2 metros (%)": 55.0,
      "Temperatura a 2 metros (ºC)": 30.0
    }
  ]
}
```

**Resposta:**
```json
{
  "predictions": [
    {"Rendimento_Predito": 8.12},
    {"Rendimento_Predito": 6.47}
  ]
}
```

## Deploy rápido (exemplos)
### Render.com (Docker)
1. Faça push deste diretório para um repositório no GitHub.
2. No Render, crie um **Web Service** a partir do repositório.
3. **Runtime:** Docker. **Porta:** 8000 (Render detecta automaticamente).
4. **Health check path:** `/health`.

### Railway (Dockerfile)
1. Novo projeto → Deploy from repo.
2. Railway detecta o `Dockerfile` e publica.
3. Configure a porta 8000.

> Qualquer provedor que aceite Docker vai funcionar (Fly.io, Okteto, etc.).

## Integração com a Entrega 1
- Copie `models/best_model.pkl` da Entrega 1 para `models/` aqui. A API carregará esse modelo.
- Se preferir, deixe um `data/crop_yield.csv` em `data/` que a API treina automaticamente ao iniciar.

---

**Dica:** Use `curl` para testar rapidamente:
```bash
curl -X POST http://127.0.0.1:8000/predict -H "Content-Type: application/json" -d @sample_request.json
```
