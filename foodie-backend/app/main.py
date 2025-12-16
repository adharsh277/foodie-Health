from fastapi import FastAPI

app = FastAPI(title="Food Nutrition API")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict_food(food_name: str):
    # Temporary logic (will replace with ML later)
    fake_data = {
        "egg": {"protein": 13},
        "chicken": {"protein": 27},
        "rice": {"protein": 2.7}
    }

    return fake_data.get(food_name.lower(), {"protein": "unknown"})
