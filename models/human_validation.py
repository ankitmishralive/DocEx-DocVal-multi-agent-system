

# models/human_validation.py
from typing import List
from pydantic import BaseModel, Field

class HumanValidation(BaseModel):
    claim_number: str = Field(description="Unique identifier for the claim")
    validations: List[dict] = Field(description="List of validation details for each attribute")
  
    remark: str = Field(
        ..., 
        description="A detailed remark explaining the validation outcome. If incorrect, specify what is wrong and the expected correction."
    )

class HumanValidationsList(BaseModel):
    human_validations: List[HumanValidation] = Field(description="A list of human validations for each claim.")