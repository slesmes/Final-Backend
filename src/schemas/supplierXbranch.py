from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Any, Optional, List
from fastapi import HTTPException, status

class SupplierXBranch(BaseModel):

    id: int = Field( title="SupplierXBranch ID")
    id_supplier: int = Field( tittle="ID of the supplier")
    id_branch: int = Field(title="ID of the branch")

    class Config:
        json_schema_extra = {
            "example": {
                "id_supplier": 1,
                "id_branch": 1,
            }
        }