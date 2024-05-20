from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Any, Optional, List
from fastapi import HTTPException, status

class City(BaseModel):

    id: int = Field(title="City ID")
    name: str = Field(default=None, title="City Name")
    id_department: int = Field(title="Department ID")
    postal_code: str = Field(default=None, title="Postal code of the city")

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Example City",
                "id_department": 1,
                "postal_code": "a postal code"
            }
        }