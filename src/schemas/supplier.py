from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Any, Optional, List
from fastapi import HTTPException, status

class Supplier(BaseModel):

    id: int = Field(default=None, title="Supplier ID")
    name: str = Field(default=None, title="Supplier name")
    name_seller: str = Field(default=None, tittle="the name of the person that represent a Supplier")
    status: bool = Field(default=True, title="Supplier status")
    phone: str = Field(default=None, title="User Phone")
    id_supplierXbranch: int = Field(default=True, title="ID of the supplierXbranch")

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Example name",
                "name_seller": "Example name seller",
                "status": "true or false",
                "phone": "Example Phone",
                "id_supplierbranch": 1,
            }
        }