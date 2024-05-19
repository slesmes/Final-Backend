from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Any, Optional, List
from fastapi import HTTPException, status

class Category(BaseModel):

    id: int = Field(default=None, title="Category ID")
    name: str = Field(default=None, title="Category Name")
    description: str = Field(default=None, title="Category Description")
    id_company: int = Field(default=None, title="Company ID")

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Example Category",
                "description": "This is an example category",
                "id_company": "company_id"
            }
        }