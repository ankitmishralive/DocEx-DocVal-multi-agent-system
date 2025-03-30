

# models/claim_details.py
from typing import List, Optional
from pydantic import BaseModel, Field

class ClaimDetails(BaseModel):
    claim_number: Optional[str] = Field(description="Unique identifier for the claim", default=None)
    claim_status: Optional[str] = Field(default=None, description="Status of the claim")
    closed_date: Optional[str] = Field(default=None, description="Closed Date Mentioned in the claim")

    date_of_loss: Optional[str] = Field(description="Date when the loss occurred", default=None)
    date_reported: Optional[str] = Field(description="Date when the claim was reported")
    days_between: Optional[int] = Field(description="Number of days between the loss and another event", default=None)

    description_of_loss: Optional[str] = Field(description="Brief summary of the loss event", default=None)
    cause_of_loss: Optional[str] = Field(description="Cause of the loss")
    loss_state_loc_veh_num: Optional[str] = Field(description="Loss state/location/vehicle number", default=None)

    claimant_name: Optional[str] = Field(default=None, description="Name of the claimant, if available")
    driver_class_cd: Optional[str] = Field(description="Driver class code", default=None)
    loss_subline: Optional[str] = Field(description="Loss subline information", default=None)

    indemnity_paid: Optional[float] = Field(description="Amount paid for indemnity, if any", default=None)
    indemnity_reserve: Optional[float] = Field(description="Amount reserved for indemnity", default=None)
    indemnity_incurred: Optional[float] = Field(description="Amount incurred for indemnity", default=None)

    medical_paid: Optional[float] = Field(description="Amount paid for medical expenses, if any", default=None)
    medical_reserve: Optional[float] = Field(description="Amount reserved for medical expenses", default=None)
    medical_incurred: Optional[float] = Field(description="Amount incurred for medical expenses", default=None)

    expense_paid: Optional[float] = Field(description="Other expenses paid, if any", default=None)
    expense_reserve: Optional[float] = Field(description="Amount reserved for expenses", default=None)
    expense_incurred: Optional[float] = Field(description="Amount incurred for expenses", default=None)

    subro_salvage: Optional[str] = Field(default=None, description="Amount for Subro/Salvage, if any")
    deductible_recovery: Optional[str] = Field(description="Amount for Deductible/Recovery, if any", default=None)

    total_paid: Optional[float] = Field(description="Total amount paid for the claim", default=None)
    total_reserve: Optional[float] = Field(description="Total amount reserved for the claim", default=None)
    total_incurred: Optional[float] = Field(description="Total amount incurred for the claim", default=None)

class ClaimsList(BaseModel):
    claims: List[ClaimDetails] = Field(description="A list of claim details extracted from the document.")