
import json, pathlib, sys
from fastapi.testclient import TestClient

# Allow running tests when project root is current working directory
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json().get("health") == "ok"

def test_predict():
    payload = {
        "items": [{
            "Cultura": "Cultura_1",
            "Precipitação (mm dia 1)": 4.5,
            "Umidade específica a 2 metros (g/kg)": 7.0,
            "Umidade relativa a 2 metros (%)": 65.0,
            "Temperatura a 2 metros (ºC)": 22.0
        }]
    }
    r = client.post("/predict", json=payload)
    assert r.status_code == 200
    data = r.json()
    assert "predictions" in data
    assert isinstance(data["predictions"][0]["Rendimento_Predito"], float)
