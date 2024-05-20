from fastapi import APIRouter
from src.schemas.supplierXpart import SupplierXpart
from fastapi import FastAPI, Body, Query, Path
from fastapi.responses import HTMLResponse, JSONResponse
from typing import Any, Optional, List
from src.config.database import SessionLocal
from src.models.supplierXpart import Supplierxpart as supplierXpartModel
from fastapi.encoders import jsonable_encoder
from src.repositories.supplierXpart import supplierXpartRepository
supplierXpart_router = APIRouter()


@supplierXpart_router.get('/',
    tags=['supplierXpart'],
    response_model=List[SupplierXpart],
    description="Returns all supplierXpart ")
def get_all_supplierXparts() -> List[SupplierXpart]:
    db = SessionLocal()
    result = supplierXpartRepository(db).get_all_supplierXparts()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@supplierXpart_router.get('/{id}',
    tags=['supplierXpart'],
    response_model=SupplierXpart,
    description="Returns data of one specific supplierXpart")
def get_supplierXpart_by_id(id: int = Path(ge=0, le=5000)) -> SupplierXpart:
    db = SessionLocal()
    element = supplierXpartRepository(db).get_supplierXpart(id)
    if not element:
        return JSONResponse(content={
            "message": "The requested supplierXpart was not found",
            "data": None
        }, status_code=400)
    
    return JSONResponse(content=jsonable_encoder(element),status_code=200)

@supplierXpart_router.post('/',
    tags=['supplierXpart'],
    response_model=dict,
    description="Creates a new supplierXpart")
def create_supplierXpart(supplierXpart: SupplierXpart) -> dict:
    db = SessionLocal()
    new_supplierXpart = supplierXpartRepository(db).create_supplierXpart(supplierXpart)
    return JSONResponse(content={
        "message": "The supplierXpart was successfully created",
        "data": jsonable_encoder(new_supplierXpart)
    }, status_code=201)

@supplierXpart_router.delete('/{id}',
    tags=['supplierXpart'],
    response_model=dict,
    description="Removes specific supplierXpart")
def remove_supplierXpart(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    element = supplierXpartRepository(db).get_supplierXpart(id)
    if not element:
        return JSONResponse(content={
            "message": "The requested supplierXpart was not found",
            "data": None
        }, status_code=404)
    supplierXpartRepository(db).remove_supplierXpart(id)
    return JSONResponse(content={
        "message": "The supplierXpart was removed successfully",
        "data": None
    }, status_code=200)