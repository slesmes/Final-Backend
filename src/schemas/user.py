from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Any, Optional, List
from fastapi import HTTPException, status

class User(BaseModel):

    identification: str = Field(title="User identification")
    name: str = Field(default=None, title="User Name")
    lastname: str = Field(default=None, title="User lastname")
    username: str = Field(default=None, tittle="Username of the user")
    password: str = Field(default=None, tittle="User Password")
    status: bool = Field(default=True, title="User Status")
    email: str = Field(default=None, title="User email")
    phone: str = Field(default=None, title="User Phone")
    id_branch: int = Field( title="id of the branch")
    id_rol: int = Field( title="id of the rol")

    class Config:
        json_schema_extra = {
            "example": {
                "identification": "1004367716",
                "name": "Andres",
                "lastname": "Perez",
                "username": "andre1438",
                "password": "hola123",
                "status": 1,
                "email": "andresap2017@gmail.com",
                "phone": "3134902138",
                "id_branch": 1,
                "id_rol": 1,
            }
        }

class LoginUser(BaseModel):

    username: str = Field(default=None, tittle="Username of the user")
    password: str = Field(default=None, tittle="User Password")

    class Config:
        json_schema_extra = {
            "example": {
                "username": "andre1438",
                "password": "hola123"
            }
        }