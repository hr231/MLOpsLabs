from pathlib import Path
import joblib
from typing import Any, Dict

HERE = Path(__file__).resolve().parent
MODEL_PATH = (HERE / ".." / "model" / "diabetes_model.pkl").resolve()

_MODEL_CACHE: Dict[str, Any] | None = None

def load_model() -> Dict[str, Any]:
    global _MODEL_CACHE
    if _MODEL_CACHE is None:
        if not MODEL_PATH.exists():
            raise FileNotFoundError(
                f"Model file not found at {MODEL_PATH}. Run `python train.py` first."
            )
        _MODEL_CACHE = joblib.load(MODEL_PATH)
    return _MODEL_CACHE
