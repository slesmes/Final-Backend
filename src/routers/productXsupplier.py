from fastapi import APIRouter
from src.schemas.productXsupplier import ProductXsupplier
from fastapi import FastAPI, Body, Query, Path
from fastapi.responses import HTMLResponse, JSONResponse
from typing import Annotated, Any, Optional, List
from src.config.database import SessionLocal
from src.models.productXsupplier import Productxsupplier as productXsupplierModel
from fastapi.encoders import jsonable_encoder
from src.repositories.productXsupplier import productXsupplierRepository
from src.auth.has_access import security
from fastapi.security import HTTPAuthorizationCredentials
from fastapi import APIRouter, Body, Depends, Query, Path, Security, status
productXsupplier_router = APIRouter()


@productXsupplier_router.get('/',
    tags=['ProductXsupplier'],
    response_model=List[ProductXsupplier],
    description="Returns all productXsupplier ")
def get_all_productXsuppliers(credentials: HTTPAuthorizationCredentials = Security(security)) -> List[ProductXsupplier]:
    db = SessionLocal()
    result = productXsupplierRepository(db).get_all_productXsuppliers()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@productXsupplier_router.get('/{id}',
    tags=['ProductXsupplier'],
    response_model=ProductXsupplier,
    description="Returns data of one specific productXsupplier")
def get_productXsupplier_by_id(id: int = Path(ge=0, le=5000), credentials: HTTPAuthorizationCredentials = Security(security)) -> ProductXsupplier:
    db = SessionLocal()
    element = productXsupplierRepository(db).get_productXsupplier(id)
    if not element:
        return JSONResponse(content={
            "message": "The requested productXsupplier was not found",
            "data": None
        }, status_code=400)
    
    return JSONResponse(content=jsonable_encoder(element),status_code=200)

@productXsupplier_router.post('/',
    tags=['ProductXsupplier'],
    response_model=dict,
    description="Creates a new productXsupplier")
def create_productXsupplier(productXsupplier: ProductXsupplier, credentials: HTTPAuthorizationCredentials = Security(security)) -> dict:
    db = SessionLocal()
    new_productXsupplier = productXsupplierRepository(db).create_productXsupplier(productXsupplier)
    return JSONResponse(content={
        "message": "The productXsupplier was successfully created",
        "data": jsonable_encoder(new_productXsupplier)
    }, status_code=201)

@productXsupplier_router.put('{id}', tags=['ProductXsupplier'],
    response_model=dict,
    description="Update a new ProductXsupplier")
def update_productXsupplier(credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)],id:int = Path(ge=1), productXsupplier: ProductXsupplier = Body()) -> dict:
    db= SessionLocal()
    update_productXsupplier = productXsupplierRepository(db).update_productXsupplier(id,productXsupplier)
    return JSONResponse(
        content={        
        "message": "The productXsupplier was successfully updated",        
        "data": jsonable_encoder(update_productXsupplier)    
        }, 
        status_code=status.HTTP_201_CREATED
    )


@productXsupplier_router.delete('/{id}',
    tags=['ProductXsupplier'],
    response_model=dict,
    description="Removes specific productXsupplier")
def remove_productXsupplier(id: int = Path(ge=1), credentials: HTTPAuthorizationCredentials = Security(security)) -> dict:
    db = SessionLocal()
    element = productXsupplierRepository(db).get_productXsupplier(id)
    if not element:
        return JSONResponse(content={
            "message": "The requested productXsupplier was not found",
            "data": None
        }, status_code=404)
    productXsupplierRepository(db).delete_productXsupplier(id)
    return JSONResponse(content={
        "message": "The productXsupplier was removed successfully",
        "data": None
    }, status_code=200)