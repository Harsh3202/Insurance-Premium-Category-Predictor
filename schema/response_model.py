from pydantic import BaseModel,Field,computed_field,field_validator
from typing import Literal, Optional

class Response(BaseModel):
    prediction_category: str = Field(..., description="Predicted insurance premium category", example="Low")
    confidence: float = Field(..., description="Confidence score of the prediction (Range: 0-1)", example=0.66)
    class_probabilities: dict[str, float] = Field(..., description="Class probabilities for each category", example={"Low": 0.8, "Medium": 0.15, "High": 0.05})