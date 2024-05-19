from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Any, Optional, List
from fastapi import HTTPException, status

class Part(BaseModel):

    id: int = Field(default=None, title="Part ID")
    name: str = Field(default=None, title="Part name")
    quantity: int = Field(default=None, tittle="Part quantity")
    price: int = Field(default=None, title="Part price")
    id_branch: int = Field(default=None, title="ID of the company")

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Example name",
                "quantity": 340,
                "price": 5550,
                "id_branch": 1,
            }
        }