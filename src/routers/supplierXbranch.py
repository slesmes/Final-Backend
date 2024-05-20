from fastapi import APIRouter
from src.schemas.supplierXbranch import SupplierXBranch
from fastapi import FastAPI, Body, Query, Path
from fastapi.responses import HTMLResponse, JSONResponse
from typing import Any, Optional, List
from src.config.database import SessionLocal
from src.models.supplierXbranch import Supplierxbranch as supplierXbranchModel
from fastapi.encoders import jsonable_encoder
from src.repositories.supplierXbranch import supplierXbranchRepository
supplierXbranch_router = APIRouter()


@supplierXbranch_router.get('/',
    tags=['supplierXbranch'],
    response_model=List[SupplierXBranch],
    description="Returns all supplierXbranch ")
def get_all_supplierXbranchs() -> List[SupplierXBranch]:
    db = SessionLocal()
    result = supplierXbranchRepository(db).get_all_supplierXbranchs()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@supplierXbranch_router.get('/{id}',
    tags=['supplierXbranch'],
    response_model=SupplierXBranch,
    description="Returns data of one specific supplierXbranch")
def get_supplierXbranch_by_id(id: int = Path(ge=0, le=5000)) -> SupplierXBranch:
    db = SessionLocal()
    element = supplierXbranchRepository(db).get_supplierXbranch(id)
    if not element:
        return JSONResponse(content={
            "message": "The requested supplierXbranch was not found",
            "data": None
        }, status_code=400)
    
    return JSONResponse(content=jsonable_encoder(element),status_code=200)

@supplierXbranch_router.post('/',
    tags=['supplierXbranch'],
    response_model=dict,
    description="Creates a new supplierXbranch")
def create_supplierXbranch(supplierXbranch: SupplierXBranch) -> dict:
    db = SessionLocal()
    new_supplierXbranch = supplierXbranchRepository(db).create_supplierXbranch(supplierXbranch)
    return JSONResponse(content={
        "message": "The supplierXbranch was successfully created",
        "data": jsonable_encoder(new_supplierXbranch)
    }, status_code=201)

@supplierXbranch_router.delete('/{id}',
    tags=['supplierXbranch'],
    response_model=dict,
    description="Removes specific supplierXbranch")
def remove_supplierXbranch(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    element = supplierXbranchRepository(db).get_supplierXbranch(id)
    if not element:
        return JSONResponse(content={
            "message": "The requested supplierXbranch was not found",
            "data": None
        }, status_code=404)
    supplierXbranchRepository(db).delete_supplierXbranch(id)
    return JSONResponse(content={
        "message": "The supplierXbranch was removed successfully",
        "data": None
    }, status_code=200)