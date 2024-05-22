from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Any, Optional, List
from fastapi import HTTPException, status

class Category(BaseModel):

    id: int = Field(default=None, title="Category ID")
    name: str = Field(default=None, title="Category Name")
    description: str = Field(default=None, title="Category Description")
    id_branch: int = Field(default=None, title="ID of the branch")
    status: bool = Field(default=True, title="Category status")

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Example Category",
                "description": "This is an example category"
            }
        }