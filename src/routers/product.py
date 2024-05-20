from fastapi import APIRouter
from src.schemas.product import Product
from fastapi import FastAPI, Body, Query, Path
from fastapi.responses import HTMLResponse, JSONResponse
from typing import Any, Optional, List
from src.config.database import SessionLocal
from src.models.product import Product as productModel
from fastapi.encoders import jsonable_encoder
from src.repositories.product import productRepository
product_router = APIRouter()


@product_router.get('/',
    tags=['product'],
    response_model=List[Product],
    description="Returns all product ")
def get_all_products() -> List[Product]:
    db = SessionLocal()
    result = productRepository(db).get_all_products()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@product_router.get('/{id}',
    tags=['product'],
    response_model=Product,
    description="Returns data of one specific product")
def get_product_by_id(id: int = Path(ge=0, le=5000)) -> Product:
    db = SessionLocal()
    element = productRepository(db).get_product(id)
    if not element:
        return JSONResponse(content={
            "message": "The requested product was not found",
            "data": None
        }, status_code=400)
    
    return JSONResponse(content=jsonable_encoder(element),status_code=200)

@product_router.post('/',
    tags=['product'],
    response_model=dict,
    description="Creates a new product")
def create_product(product: Product) -> dict:
    db = SessionLocal()
    new_product = productRepository(db).create_product(product)
    return JSONResponse(content={
        "message": "The product was successfully created",
        "data": jsonable_encoder(new_product)
    }, status_code=201)

@product_router.delete('/{id}',
    tags=['product'],
    response_model=dict,
    description="Removes specific product")
def remove_product(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    element = productRepository(db).get_product(id)
    if not element:
        return JSONResponse(content={
            "message": "The requested product was not found",
            "data": None
        }, status_code=404)
    productRepository(db).delete_product(id)
    return JSONResponse(content={
        "message": "The product was removed successfully",
        "data": None
    }, status_code=200)