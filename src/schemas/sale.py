from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Any, Optional, List
from fastapi import HTTPException, status

class Sale(BaseModel):

    id: int = Field( title="Sale ID")
    id_product: int = Field( title="ID of the product")
    id_bill: int = Field(tittle="ID of the bill")
    quantity: int = Field(default=None, title="quantity of the product")
    id_branch: int = Field(tittle="ID of the branch")


    class Config:
        json_schema_extra = {
            "example": {
                "id_product": 1,
                "id_bill": 1,
                "quantity": 240
            }
        }