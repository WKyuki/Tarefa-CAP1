
import os
import joblib
import numpy as np
import pandas as pd
from pathlib import Path

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor

RANDOM_STATE = 42

BASE_DIR = Path(os.getenv("BASE_DIR", "/mnt/data/FarmTech_Fase5_Entrega2_Cloud"))
MODELS_DIR = Path(os.getenv("MODELS_DIR", BASE_DIR / "models"))
DATA_DIR = Path(os.getenv("DATA_DIR", BASE_DIR / "data"))
MODEL_PATH = Path(os.getenv("MODEL_PATH", MODELS_DIR / "best_model.pkl"))

FEATURES = ['Cultura',
            'Precipitação (mm dia 1)',
            'Umidade específica a 2 metros (g/kg)',
            'Umidade relativa a 2 metros (%)',
            'Temperatura a 2 metros (ºC)']
TARGET = 'Rendimento'

def _generate_synthetic_dataset(n=600, n_culturas=5, random_state=RANDOM_STATE):
    rng = np.random.default_rng(random_state)
    culturas = [f'Cultura_{i+1}' for i in range(n_culturas)]
    cultura = rng.choice(culturas, size=n, replace=True)

    precipitacao = rng.normal(4.0, 2.0, size=n).clip(0, 20)
    umid_espec = rng.normal(7.0, 1.8, size=n).clip(2, 15)
    umid_rel = rng.normal(65, 15, size=n).clip(10, 100)
    temp2m = rng.normal(22, 6, size=n).clip(-2, 42)

    base_yield = (
        0.8*precipitacao
        + 0.3*umid_espec
        - 0.15*np.maximum(temp2m-28, 0)**2 / 10
        + 0.02*umid_rel
    )
    efeitos = {c: rng.normal(3.0 + i*0.5, 0.4) for i, c in enumerate(culturas)}
    rendimento = np.array([base_yield[i] + efeitos[cultura[i]] + rng.normal(0, 0.8) for i in range(n)])
    rendimento = rendimento.clip(0.5, None)

    df = pd.DataFrame({
        'Cultura': cultura,
        'Precipitação (mm dia 1)': np.round(precipitacao, 2),
        'Umidade específica a 2 metros (g/kg)': np.round(umid_espec, 2),
        'Umidade relativa a 2 metros (%)': np.round(umid_rel, 1),
        'Temperatura a 2 metros (ºC)': np.round(temp2m, 1),
        'Rendimento': np.round(rendimento, 2)
    })
    return df

def build_preprocessor():
    cat_cols = ['Cultura']
    num_cols = [c for c in FEATURES if c not in cat_cols]
    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, num_cols),
            ('cat', categorical_transformer, cat_cols)
        ]
    )
    return preprocessor

def train_and_save_model(df: pd.DataFrame, path: Path = MODEL_PATH):
    X = df[FEATURES].copy()
    y = df[TARGET].values
    preprocessor = build_preprocessor()
    model = RandomForestRegressor(n_estimators=300, random_state=RANDOM_STATE)
    pipe = Pipeline(steps=[('prep', preprocessor), ('model', model)])
    pipe.fit(X, y)
    path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(pipe, path)
    return pipe

def load_or_train_model():
    # Priority 1: existing model path
    if MODEL_PATH.exists():
        try:
            pipe = joblib.load(MODEL_PATH)
            return pipe, "loaded_existing"
        except Exception:
            pass
    # Priority 2: train using provided CSV if available
    csv_path = DATA_DIR / "crop_yield.csv"
    if csv_path.exists():
        try:
            df = pd.read_csv(csv_path)
            df = df[[*FEATURES, TARGET]]
            pipe = train_and_save_model(df, MODEL_PATH)
            return pipe, "trained_from_csv"
        except Exception:
            pass
    # Priority 3: train on synthetic
    df_syn = _generate_synthetic_dataset()
    pipe = train_and_save_model(df_syn, MODEL_PATH)
    return pipe, "trained_synthetic"
