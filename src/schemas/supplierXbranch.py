from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Any, Optional, List
from fastapi import HTTPException, status

class SupplierXBranch(BaseModel):

    id: int = Field(default=None, title="SupplierXBranch ID")
    id_supplier: int = Field(default=None, tittle="ID of the supplier")
    id_branch: int = Field(default=None, title="ID of the branch")

    class Config:
        json_schema_extra = {
            "example": {
                "id_supplier": 1,
                "id_branch": 1,
            }
        }