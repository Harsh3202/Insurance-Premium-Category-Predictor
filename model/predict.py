import pickle
import pandas as pd

with open('model\model.pkl', 'rb') as f:
    model = pickle.load(f)

MODEL_VERSION = "1.0.0"
class_label  = model.classes_.tolist()

def predict(input_data: dict):
    
    input_df = pd.DataFrame([input_data])

    prediction_class = model.predict(input_df)[0]
    
    probabilities = model.predict_proba(input_df)[0]
    confidence = max(probabilities)

    class_probs = dict(zip(class_label, map(lambda p: round(p,4), probabilities)))
    return {
        "prediction_category": prediction_class,
        "confidence": confidence,
        "class_probabilities": class_probs
    }