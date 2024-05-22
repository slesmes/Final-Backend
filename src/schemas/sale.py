from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Any, Optional, List
from fastapi import HTTPException, status

class Sale(BaseModel):

    id: int = Field(default=None, title="Sale ID")
    id_product: int = Field(default=None, title="ID of the product")
    id_bill: int = Field(default=None, tittle="ID of the bill")
    quantity: int = Field(default=None, title="quantity of the product")
    id_branch: int = Field(default=None, tittle="ID of the branch")


    class Config:
        json_schema_extra = {
            "example": {
                "id_product": 1,
                "id_bill": 1,
                "quantity": 240
            }
        }