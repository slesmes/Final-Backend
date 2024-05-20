from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Any, Optional, List
from fastapi import HTTPException, status

class Department(BaseModel):

    id: int = Field(title="Department ID")
    name: str = Field(default=None, title="Department Name")
    id_country: int = Field(title="Country ID")

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Example name",
                "id_country": 1,
            }
        }