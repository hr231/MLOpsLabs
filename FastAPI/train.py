from pathlib import Path
import joblib
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error

HERE = Path(__file__).resolve().parent
MODEL_DIR = (HERE / ".." / "model").resolve()
MODEL_DIR.mkdir(parents=True, exist_ok=True)
MODEL_PATH = MODEL_DIR / "diabetes_model.pkl"

def main() -> None:
    data = load_diabetes()
    X, y = data.data, data.target

    X_tr, X_te, y_tr, y_te = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    reg = RandomForestRegressor(
        n_estimators=250, random_state=42, n_jobs=-1
    )
    reg.fit(X_tr, y_tr)

    preds = reg.predict(X_te)
    r2 = r2_score(y_te, preds)
    mae = mean_absolute_error(y_te, preds)
    print(f"R^2: {r2:.3f} | MAE: {mae:.2f}")

    payload = {
        "model": reg,
        "feature_names": list(data.feature_names),
        "target_name": "disease_progression_index"
    }
    joblib.dump(payload, MODEL_PATH)
    print(f"saved model to: {MODEL_PATH}")

if __name__ == "__main__":
    main()
