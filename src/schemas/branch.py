from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Any, Optional, List
from fastapi import HTTPException, status

class Branch(BaseModel):

    id: int = Field(title="Branch id")
    name: str = Field(default=None, title="Branch Name")
    id_city: int = Field(title="ID of the city")
    id_company: int = Field(title="ID of the company")
    address: str = Field(default=None, tittle="Adress of the branch")
    phone: str = Field(default=None, tittle="Phone of the branch")
    status: bool = Field(default=True, title="Branch status")

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Example Company",
                "id_city": 1,
                "address": "Example addess",
                "phone": "Example Phone",
                "id_company": 1,
                "status": "True or false"
            }
        }