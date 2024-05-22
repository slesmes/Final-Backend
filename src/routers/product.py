from fastapi import APIRouter
from src.schemas.product import Product
from fastapi import FastAPI, Body, Query, Path
from fastapi.responses import HTMLResponse, JSONResponse
from typing import Annotated, Any, Optional, List
from src.config.database import SessionLocal
from src.models.product import Product as productModel
from fastapi.encoders import jsonable_encoder
from src.repositories.product import productRepository
from src.auth.has_access import security
from src.auth import auth_handler
from fastapi.security import HTTPAuthorizationCredentials
from fastapi import APIRouter, Body, Depends, Query, Path, Security, status
product_router = APIRouter()


@product_router.get('/',
    tags=['product'],
    response_model=List[Product],
    description="Returns all product ")
def get_all_products(credentials: HTTPAuthorizationCredentials = Security(security)) -> List[Product]:
    db = SessionLocal()
    token = credentials.credentials
    payload = auth_handler.decode_token(token=token)
    branch = payload.get("user.branch")
    result = productRepository(db).get_all_products(branch)
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@product_router.get('/{id}',
    tags=['product'],
    response_model=Product,
    description="Returns data of one specific product")
def get_product_by_id(id: int = Path(ge=0, le=5000), credentials: HTTPAuthorizationCredentials = Security(security)) -> Product:
    db = SessionLocal()
    token = credentials.credentials
    payload = auth_handler.decode_token(token=token)
    branch = payload.get("user.branch")
    element = productRepository(db).get_product(id, branch)
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
def create_product(product: Product, credentials: HTTPAuthorizationCredentials = Security(security)) -> dict:
    db = SessionLocal()
    token = credentials.credentials
    payload = auth_handler.decode_token(token=token)
    product.id_branch = payload.get("user.branch")
    new_product = productRepository(db).create_product(product)
    return JSONResponse(content={
        "message": "The product was successfully created",
        "data": jsonable_encoder(new_product)
    }, status_code=201)

@product_router.put('{id}', tags=['product'],
    response_model=dict,
    description="Update a new product")
def update_part(credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)],id:int = Path(ge=1), product: Product = Body()) -> dict:
    db= SessionLocal()
    update_product = productRepository(db).update_product(id,product)
    return JSONResponse(
        content={        
        "message": "The product was successfully updated",        
        "data": jsonable_encoder(update_product)    
        }, 
        status_code=status.HTTP_201_CREATED
    )

@product_router.delete('/{id}',
    tags=['product'],
    response_model=dict,
    description="Removes specific product")
def remove_product(id: int = Path(ge=1), credentials: HTTPAuthorizationCredentials = Security(security)) -> dict:
    db = SessionLocal()
    token = credentials.credentials
    payload = auth_handler.decode_token(token=token)
    branch = payload.get("user.branch")
    element = productRepository(db).get_product(id, branch)
    if not element:
        return JSONResponse(content={
            "message": "The requested product was not found",
            "data": None
        }, status_code=404)
    productRepository(db).delete_product(id, branch)
    return JSONResponse(content={
        "message": "The product was removed successfully",
        "data": None
    }, status_code=200)