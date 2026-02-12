"""FastAPI service for GridGuard AI."""

from fastapi import FastAPI
from pydantic import BaseModel, Field

from ai.inference import predict_next_load
from recommendation.rule_engine import recommend_actions
from risk.blackout_probability import risk_score
from risk.overload_model import overload_index

app = FastAPI(title="GridGuard AI", version="0.1.0")


class PredictRequest(BaseModel):
    features: list[float] = Field(default_factory=list)
    transformer_capacity: float = 500.0
    anomaly_score: float = 0.1
    voltage_deviation: float = 0.05


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/predict")
def predict(payload: PredictRequest) -> dict:
    inference = predict_next_load(payload.features)
    ov_idx = overload_index(inference["predicted_load"], payload.transformer_capacity)
    composite_risk = risk_score(ov_idx, payload.anomaly_score, payload.voltage_deviation)
    actions = recommend_actions(ov_idx)
    return {
        **inference,
        "overload_index": round(ov_idx, 3),
        "risk_score": round(composite_risk, 3),
        "actions": actions,
    }
