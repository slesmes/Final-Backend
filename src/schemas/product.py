from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Any, Optional, List
from fastapi import HTTPException, status

class Product(BaseModel):

    id: int = Field( title="Product ID")
    name: str = Field(default=None, title="Product name")
    price: int = Field(default=None, tittle="Product price")
    quantity: int = Field(default=None, title="Product quantity")
    description: str = Field(default=None, title="Product description")
    id_category: int = Field(title="ID of the category")
    id_branch: int = Field(tittle="ID of the branch")
    status: bool = Field(default=True, title="Product status")
    disccount: float = Field(default=None, title="Product disccount")

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Example name",
                "price": 5000,
                "quantity": 240,
                "description": "Example of description",
                "id_category": 1,
                "id_status": "true or false",
                "id_supplier": 1,
            }
        }