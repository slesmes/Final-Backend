from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Any, Optional, List
from fastapi import HTTPException, status

class User(BaseModel):

    identification: int = Field(default=None, title="User identification")
    name: str = Field(default=None, title="User Name")
    lastname: str = Field(default=None, title="User lastname")
    username: str = Field(default=None, tittle="Username of the user")
    password: str = Field(default=None, tittle="User Password")
    status: bool = Field(default=True, title="User Status")
    email: str = Field(default=None, title="User email")
    phone: str = Field(default=None, title="User Phone")
    id_branch: int = Field(default=None, title="id of the branch")
    id_rol: int = Field(default=None, title="id of the rol")

    class Config:
        json_schema_extra = {
            "example": {
                "identification": "Example identification",
                "name": "Example name",
                "lastname": "Example lastname",
                "username": "Example username",
                "password": "Example password",
                "status": "true or false",
                "email": "Example email",
                "phone": "Example Phone",
                "id_branch": 1,
                "id_rol": 1,
            }
        }