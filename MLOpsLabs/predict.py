from typing import Sequence
import numpy as np
from data import load_model

def predict_value(features: Sequence[float]) -> float:
    if len(features) != 10:
        raise ValueError(f"Expected 10 features, got {len(features)}")
    
    features_array = np.array(features, dtype=float)
    payload = load_model()
    reg = payload["model"]
    y_hat = reg.predict(features_array.reshape(1, -1))[0]
    
    return float(y_hat)
