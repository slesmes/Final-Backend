from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Any, Optional, List
from fastapi import HTTPException, status

class Rol(BaseModel):

    id: int = Field( title="Rol ID")
    name: str = Field(default=None, title="Rol Name")
    description: str = Field(default=None, title="Rol Description")
    id_branch: int = Field(default='', title="ID of the branch")

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Example Rol",
                "description": "This is an example Rol"
            }
        }