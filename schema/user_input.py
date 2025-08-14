from pydantic import BaseModel,Field,computed_field,field_validator
from typing import Literal, Optional,Annotated
from config.city_tier import tier_1_cities, tier_2_cities




class UserInput(BaseModel):

    age: Annotated[int, Field(..., gt=0,lt = 120, description="Age of the user in years")]
    weight: Annotated[float, Field(..., gt=0, description="Weight of the user in kg")]
    height: Annotated[float, Field(..., gt=0,lt = 2.5, description="Height of the user in m")]
    income_lpa: Annotated[float, Field(..., gt=0, description="Income of the user in LPA")]
    smoker: Annotated[bool, Field(..., description="Is the user a smoker?")]
    city: Annotated[str, Field(..., description="City of the user")]
    occupation: Annotated[Literal['retired', 'freelancer', 'student', 'government_job',
       'business_owner', 'unemployed', 'private_job'], Field(..., description="Occupation of the user")]


    @computed_field
    @property
    def bmi(self) -> float:
        return self.weight / (self.height ** 2)
    
    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return "High"
        elif self.smoker or self.bmi > 27:
            return "Medium"
        else:
            return "Low"

    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return "Young"
        elif self.age < 45:
            return "Adult"
        elif self.age < 60:
            return "Middle age"
        else:
            return "Senior"
     
    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3
        
    @field_validator('city')
    @classmethod
    def normalize_city(cls, v: str) -> str:
        return v.strip().title()