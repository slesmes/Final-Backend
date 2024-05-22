from fastapi import APIRouter
from src.schemas.productXpart import ProductXpart
from fastapi import FastAPI, Body, Query, Path
from fastapi.responses import HTMLResponse, JSONResponse
from typing import Annotated, Any, Optional, List
from src.config.database import SessionLocal
from src.models.productXpart import Productxpart as productXpartModel
from fastapi.encoders import jsonable_encoder
from src.repositories.productXpart import productXpartRepository
from src.auth import auth_handler
from src.auth.has_access import security
from fastapi.security import HTTPAuthorizationCredentials
from fastapi import APIRouter, Body, Depends, Query, Path, Security, status
productXpart_router = APIRouter()


@productXpart_router.get('/',
    tags=['productXpart'],
    response_model=List[ProductXpart],
    description="Returns all productXpart ")
def get_all_productXparts(credentials: HTTPAuthorizationCredentials = Security(security)) -> List[ProductXpart]:
    db = SessionLocal()
    token = credentials.credentials
    payload = auth_handler.decode_token(token=token)
    branch = payload.get("user.branch")
    result = productXpartRepository(db).get_all_productXparts(branch)
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@productXpart_router.get('/{id}',
    tags=['productXpart'],
    response_model=ProductXpart,
    description="Returns data of one specific productXpart")
def get_productXpart_by_id(id: int = Path(ge=0, le=5000), credentials: HTTPAuthorizationCredentials = Security(security)) -> ProductXpart:
    db = SessionLocal()
    token = credentials.credentials
    payload = auth_handler.decode_token(token=token)
    branch = payload.get("user.branch")
    element = productXpartRepository(db).get_productXpart(id, branch)
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
def create_productXpart(productXpart: ProductXpart, credentials: HTTPAuthorizationCredentials = Security(security)) -> dict:
    db = SessionLocal()
    new_productXpart = productXpartRepository(db).create_productXpart(productXpart)
    return JSONResponse(content={
        "message": "The productXpart was successfully created",
        "data": jsonable_encoder(new_productXpart)
    }, status_code=201)

@productXpart_router.put('{id}', tags=['productXpart'],
    response_model=dict,
    description="Update a new part")
def update_productXpart(credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)],id:int = Path(ge=1), productXpart: ProductXpart = Body()) -> dict:
    db= SessionLocal()
    update_productXpart = productXpartRepository(db).update_productXPart(id,productXpart)
    return JSONResponse(
        content={        
        "message": "The productXpart was successfully updated",        
        "data": jsonable_encoder(update_productXpart)    
        }, 
        status_code=status.HTTP_201_CREATED
    )


@productXpart_router.delete('/{id}',
    tags=['productXpart'],
    response_model=dict,
    description="Removes specific productXpart")
def remove_productXpart(id: int = Path(ge=1), credentials: HTTPAuthorizationCredentials = Security(security)) -> dict:
    db = SessionLocal()
    token = credentials.credentials
    payload = auth_handler.decode_token(token=token)
    branch = payload.get("user.branch")
    element = productXpartRepository(db).get_productXpart(id, branch)
    if not element:
        return JSONResponse(content={
            "message": "The requested productXpart was not found",
            "data": None
        }, status_code=404)
    productXpartRepository(db).delete_productXpart(id, branch)
    return JSONResponse(content={
        "message": "The productXpart was removed successfully",
        "data": None
    }, status_code=200)