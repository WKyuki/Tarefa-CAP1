
from pydantic import BaseModel, Field
from typing import List

class YieldFeatures(BaseModel):
    Cultura: str = Field(..., description="Nome da cultura (string)")
    precip: float = Field(..., alias="Precipitação (mm dia 1)")
    umid_espec: float = Field(..., alias="Umidade específica a 2 metros (g/kg)")
    umid_rel: float = Field(..., alias="Umidade relativa a 2 metros (%)")
    temp2m: float = Field(..., alias="Temperatura a 2 metros (ºC)")

    class Config:
        allow_population_by_field_name = True

class PredictRequest(BaseModel):
    items: List[YieldFeatures]

class PredictResponseItem(BaseModel):
    Rendimento_Predito: float

class PredictResponse(BaseModel):
    predictions: List[PredictResponseItem]
