from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Any, Optional, List
from fastapi import HTTPException, status

class SupplierXpart(BaseModel):

    id: int = Field(title="SupplierXpart ID")
    id_part: int = Field( title="ID of the part")
    id_supplier: int = Field( tittle="ID of the supplier")
    id_branch: int = Field( title="ID of the branch")

    class Config:
        json_schema_extra = {
            "example": {
                "id_part": 1,
                "id_supplier": 1,
                "id_branch": 1,
            }
        }