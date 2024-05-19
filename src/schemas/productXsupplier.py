from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Any, Optional, List
from fastapi import HTTPException, status

class ProductXsupplier(BaseModel):

    id: int = Field(default=None, title="productXsupplier ID")
    id_supplier: int = Field(default=None, tittle="ID of the supplier")
    id_branch: int = Field(default=None, title="ID of the branch")
    id_product: int = Field(default=None, title="ID of the product")

    class Config:
        json_schema_extra = {
            "example": {
                "id_supplier": 1,
                "id_branch": 1,
                "id_product": 1
            }
        }