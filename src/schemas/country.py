from pydantic import BaseModel, Field, validator, model_validator
from typing import Any, Optional, List
from fastapi import HTTPException, status

class Country(BaseModel):

    id: int = Field( title="Country ID")
    name: str = Field(default=None, title="Country Name")

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Example Country",
            }
        }