
import os
from fastapi import FastAPI
from typing import List
import pandas as pd

from .schemas import PredictRequest, PredictResponse, PredictResponseItem
from .model import load_or_train_model, FEATURES

app = FastAPI(title="FarmTech Solutions — API de Rendimento de Safras",
              version="1.0.0",
              description="Serviço FastAPI para previsão de rendimento (t/ha).")

PIPELINE, MODEL_STATUS = load_or_train_model()

@app.get("/")
def root():
    return {
        "service": "FarmTech Solutions — Crop Yield API",
        "status": "ok",
        "model_status": MODEL_STATUS,
        "features": FEATURES
    }

@app.get("/health")
def health():
    return {"health": "ok"}

@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest):
    # Convert incoming items to DataFrame respecting aliases/field names
    records = []
    for item in request.items:
        # Accept both alias names and field names by using dict(by_alias=True)
        d = item.dict(by_alias=True)
        records.append(d)
    df = pd.DataFrame(records, columns=FEATURES)
    preds = PIPELINE.predict(df)
    return {"predictions": [PredictResponseItem(Rendimento_Predito=float(p)) for p in preds]}
