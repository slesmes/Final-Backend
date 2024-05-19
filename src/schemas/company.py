from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Any, Optional, List
from fastapi import HTTPException, status

class Company(BaseModel):

    nit: int = Field(default=None, title="Company Nit")
    name: str = Field(default=None, title="Company Name")
    id_city: int = Field(default=None, title="Department ID")
    address: str = Field(default=None, tittle="Adress of the company")
    phone: str = Field(default=None, tittle="Phone of the company")
    status: bool = Field(default=True, title="Status of the company")

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Example Company",
                "id_city": 1,
                "address": "Example addess",
                "phone": "Example Phone",
                "status": "True or false"
            }
        }