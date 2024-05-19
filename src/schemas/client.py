from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Any, Optional, List
from fastapi import HTTPException, status

class Client(BaseModel):

    identification: int = Field(default=None, title="Client identification")
    name: str = Field(default=None, title="Client Name")
    lastname: str = Field(default=None, title="Client lastname")
    status: bool = Field(default=True, title="Client Status")
    email: str = Field(default=None, title="Client email")
    phone: str = Field(default=None, title="Client Phone")
    id_company: int = Field(default=None, title="ID of the company")
    address: str = Field(default=None, title="Client address")
    id_city: int = Field(default=None, title="ID of the city")

    class Config:
        json_schema_extra = {
            "example": {
                "identification" "Example identification"
                "name": "Example name",
                "lastname": "Example lastname",
                "address": "Example username",
                "status": "true or false",
                "email": "Example email",
                "phone": "Example Phone",
                "id_company": 1,
                "id_city": 1,
            }
        }