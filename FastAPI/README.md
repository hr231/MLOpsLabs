# Diabetes Prediction API

A FastAPI-based machine learning service for predicting diabetes progression using a RandomForest regressor trained on the sklearn diabetes dataset.

## Features

- RESTful API for diabetes progression prediction
- RandomForest model with 250 estimators
- Input validation for 10 diabetes features
- Model caching for improved performance
- Interactive API documentation

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv fastapi_lab_env
   ```

3. Activate the virtual environment:
   ```bash
   # Windows
   fastapi_lab_env\Scripts\activate
   
   # Linux/Mac
   source fastapi_lab_env/bin/activate
   ```

4. Install dependencies:
   ```bash
   pip install -r MLOpsLabs/Req.txt
   ```

## Usage

1. Train the model:
   ```bash
   cd MLOpsLabs
   python train.py
   ```

2. Start the API server:
   ```bash
   uvicorn main:app --reload
   ```

3. Access the API:
   - API Documentation: http://localhost:8000/docs
   - Health Check: http://localhost:8000/
   - Prediction Endpoint: http://localhost:8000/predict

## API Endpoints

### GET /
Health check endpoint that returns API status and feature information.

### POST /predict
Predict diabetes progression based on 10 input features.

**Request Body:**
```json
{
  "features": [0.038, 0.051, 0.062, 0.022, -0.044, -0.035, -0.043, -0.003, 0.020, -0.018]
}
```

**Response:**
```json
{
  "prediction": 228.68
}
```

## Model Performance

- R² Score: ~0.44
- Mean Absolute Error: ~44.43

## Project Structure

```
MLOpsLabs/
├── main.py          # FastAPI application
├── train.py         # Model training script
├── predict.py       # Prediction logic
├── data.py          # Model loading utilities
├── Req.txt          # Dependencies
└── __init__.py      # Package initialization

model/
└── diabetes_model.pkl  # Trained model (generated after training)
```

## Dependencies

- FastAPI 0.115.0
- scikit-learn 1.5.2
- uvicorn 0.30.6
- joblib 1.4.2
- numpy
- pydantic