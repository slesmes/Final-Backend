from fastapi import APIRouter
from src.schemas.sale import Sale
from fastapi import FastAPI, Body, Query, Path
from fastapi.responses import HTMLResponse, JSONResponse
from typing import Any, Optional, List
from src.config.database import SessionLocal
from src.models.sale import Sale as saleModel
from fastapi.encoders import jsonable_encoder
from src.repositories.sale import saleRepository
sale_router = APIRouter()


@sale_router.get('/',
    tags=['sale'],
    response_model=List[Sale],
    description="Returns all sale ")
def get_all_sales() -> List[Sale]:
    db = SessionLocal()
    result = saleRepository(db).get_all_sales()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@sale_router.get('/{id}',
    tags=['sale'],
    response_model=Sale,
    description="Returns data of one specific sale")
def get_sale_by_id(id: int = Path(ge=0, le=5000)) -> Sale:
    db = SessionLocal()
    element = saleRepository(db).get_sale(id)
    if not element:
        return JSONResponse(content={
            "message": "The requested sale was not found",
            "data": None
        }, status_code=400)
    
    return JSONResponse(content=jsonable_encoder(element),status_code=200)

@sale_router.post('/',
    tags=['sale'],
    response_model=dict,
    description="Creates a new sale")
def create_sale(sale: Sale) -> dict:
    db = SessionLocal()
    new_sale = saleRepository(db).create_sale(sale)
    return JSONResponse(content={
        "message": "The sale was successfully created",
        "data": jsonable_encoder(new_sale)
    }, status_code=201)

@sale_router.delete('/{id}',
    tags=['sale'],
    response_model=dict,
    description="Removes specific sale")
def remove_sale(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    element = saleRepository(db).get_sale(id)
    if not element:
        return JSONResponse(content={
            "message": "The requested sale was not found",
            "data": None
        }, status_code=404)
    saleRepository(db).delete_sale(id)
    return JSONResponse(content={
        "message": "The sale was removed successfully",
        "data": None
    }, status_code=200)