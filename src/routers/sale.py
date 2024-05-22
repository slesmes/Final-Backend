from fastapi import APIRouter
from src.schemas.sale import Sale
from fastapi import FastAPI, Body, Query, Path
from fastapi.responses import HTMLResponse, JSONResponse
from typing import Annotated, Any, Optional, List
from src.config.database import SessionLocal
from src.models.sale import Sale as saleModel
from fastapi.encoders import jsonable_encoder
from src.auth import auth_handler
from src.repositories.sale import saleRepository
from src.auth.has_access import security
from fastapi.security import HTTPAuthorizationCredentials
from fastapi import APIRouter, Body, Depends, Query, Path, Security, status
sale_router = APIRouter()


@sale_router.get('/',
    tags=['sale'],
    response_model=List[Sale],
    description="Returns all sale ")
def get_all_sales(credentials: HTTPAuthorizationCredentials = Security(security)) -> List[Sale]:
    db = SessionLocal()
    token = credentials.credentials
    payload = auth_handler.decode_token(token=token)
    branch = payload.get("user.branch")
    result = saleRepository(db).get_all_sales(branch)
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@sale_router.get('/{id}',
    tags=['sale'],
    response_model=Sale,
    description="Returns data of one specific sale")
def get_sale_by_id(id: int = Path(ge=0, le=5000), credentials: HTTPAuthorizationCredentials = Security(security)) -> Sale:
    db = SessionLocal()
    token = credentials.credentials
    payload = auth_handler.decode_token(token=token)
    branch = payload.get("user.branch")
    element = saleRepository(db).get_sale(id, branch)
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
def create_sale(sale: Sale, credentials: HTTPAuthorizationCredentials = Security(security)) -> dict:
    db = SessionLocal()
    token = credentials.credentials
    payload = auth_handler.decode_token(token=token)
    sale.id_branch = payload.get("user.branch")
    new_sale = saleRepository(db).create_sale(sale)
    return JSONResponse(content={
        "message": "The sale was successfully created",
        "data": jsonable_encoder(new_sale)
    }, status_code=201)

@sale_router.put('{id}', tags=['sale'],
    response_model=dict,
    description="Update a new sale")
def update_sale(credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)],id:int = Path(ge=1), sale: Sale = Body()) -> dict:
    db= SessionLocal()
    update_sale = saleRepository(db).update_sale(id,sale)
    return JSONResponse(
        content={        
        "message": "The sale was successfully updated",        
        "data": jsonable_encoder(update_sale)    
        }, 
        status_code=status.HTTP_201_CREATED
    )



@sale_router.delete('/{id}',
    tags=['sale'],
    response_model=dict,
    description="Removes specific sale")
def remove_sale(id: int = Path(ge=1), credentials: HTTPAuthorizationCredentials = Security(security)) -> dict:
    db = SessionLocal()
    token = credentials.credentials
    payload = auth_handler.decode_token(token=token)
    branch = payload.get("user.branch")
    element = saleRepository(db).get_sale(id, branch)
    if not element:
        return JSONResponse(content={
            "message": "The requested sale was not found",
            "data": None
        }, status_code=404)
    saleRepository(db).delete_sale(id, branch)
    return JSONResponse(content={
        "message": "The sale was removed successfully",
        "data": None
    }, status_code=200)