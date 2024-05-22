from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Any, Optional, List
from fastapi import HTTPException, status

class Bill(BaseModel):

    id: int = Field(default=None, title="Bill ID")
    date_bill: str = Field(default=None, title="Bill date creation")
    id_client: str = Field(default=None, tittle="ID of the client")
    status: bool = Field(default=True, title="Bill status")
    id_user: str = Field(default=None, title="ID of the user")
    id_branch: int = Field(default=None, title="ID of the branch")

    class Config:
        json_schema_extra = {
            "example": {
                "date_bill": "2023-12-05",
                "id_client": "123456",
                "status":True
            }
        }




