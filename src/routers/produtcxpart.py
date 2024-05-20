from fastapi import APIRouter
from src.schemas.productXpart import ProductXpart
from fastapi import FastAPI, Body, Query, Path
from fastapi.responses import HTMLResponse, JSONResponse
from typing import Any, Optional, List
from src.config.database import SessionLocal
from src.models.productXpart import Productxpart as productXpartModel
from fastapi.encoders import jsonable_encoder
from src.repositories.productXpart import productXpartRepository
productXpart_router = APIRouter()


@productXpart_router.get('/',
    tags=['productXpart'],
    response_model=List[ProductXpart],
    description="Returns all productXpart ")
def get_all_productXparts() -> List[ProductXpart]:
    db = SessionLocal()
    result = productXpartRepository(db).get_all_productXparts()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@productXpart_router.get('/{id}',
    tags=['productXpart'],
    response_model=ProductXpart,
    description="Returns data of one specific productXpart")
def get_productXpart_by_id(id: int = Path(ge=0, le=5000)) -> ProductXpart:
    db = SessionLocal()
    element = productXpartRepository(db).get_productXpart(id)
    if not element:
        return JSONResponse(content={
            "message": "The requested productXpart was not found",
            "data": None
        }, status_code=400)
    
    return JSONResponse(content=jsonable_encoder(element),status_code=200)

@productXpart_router.post('/',
    tags=['productXpart'],
    response_model=dict,
    description="Creates a new productXpart")
def create_productXpart(productXpart: ProductXpart) -> dict:
    db = SessionLocal()
    new_productXpart = productXpartRepository(db).create_productXpart(productXpart)
    return JSONResponse(content={
        "message": "The productXpart was successfully created",
        "data": jsonable_encoder(new_productXpart)
    }, status_code=201)

@productXpart_router.delete('/{id}',
    tags=['productXpart'],
    response_model=dict,
    description="Removes specific productXpart")
def remove_productXpart(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    element = productXpartRepository(db).get_productXpart(id)
    if not element:
        return JSONResponse(content={
            "message": "The requested productXpart was not found",
            "data": None
        }, status_code=404)
    productXpartRepository(db).delete_productXpart(id)
    return JSONResponse(content={
        "message": "The productXpart was removed successfully",
        "data": None
    }, status_code=200)