from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from predict import predict_value
from data import load_model

app = FastAPI(
    title="Diabetes Prediction API",
    version="1.0.0",
    description="RandomForest model for diabetes progression prediction"
)

class DiabetesData(BaseModel):
    features: List[float]

class DiabetesResponse(BaseModel):
    prediction: float

@app.get("/")
def root():
    meta = load_model()
    return {
        "status": "ok",
        "message": "Diabetes prediction API running",
        "feature_names": meta["feature_names"],
        "target_name": meta["target_name"],
    }

@app.post("/predict", response_model=DiabetesResponse)
def predict(payload: DiabetesData) -> DiabetesResponse:
    try:
        y_hat = predict_value(payload.features)
        return DiabetesResponse(prediction=y_hat)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"inference failed: {e}")
