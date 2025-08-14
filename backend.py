from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from model.predict import predict, MODEL_VERSION,model
from schema.response_model import Response

app = FastAPI()


@app.get("/")  
def home():
    return {"message": "Welcome to the Insurance Premium Prediction API"}

@app.get("/health")
def health_check():
    return {"status": "OK",
            "version": MODEL_VERSION,
            "model": model is not None}

@app.post("/predict", response_model=Response)
def predict_insurance(input_data: UserInput):
    user_input ={
        "bmi": input_data.bmi,
        "age_group": input_data.age_group,
        "city_tier": input_data.city_tier,
        "income_lpa": input_data.income_lpa,
        "lifestyle_risk": input_data.lifestyle_risk,
        "occupation": input_data.occupation
    }
    try:
        prediction = predict(user_input)
        return JSONResponse(status_code=200, content={"response": prediction})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})