from fastapi import APIRouter
from src.schemas.supplierXbranch import SupplierXBranch
from fastapi import FastAPI, Body, Query, Path
from fastapi.responses import HTMLResponse, JSONResponse
from typing import Annotated, Any, Optional, List
from src.config.database import SessionLocal
from src.models.supplierXbranch import Supplierxbranch as supplierXbranchModel
from fastapi.encoders import jsonable_encoder
from src.repositories.supplierXbranch import supplierXbranchRepository
from src.auth.has_access import security
from src.auth import auth_handler
from fastapi.security import HTTPAuthorizationCredentials
from fastapi import APIRouter, Body, Depends, Query, Path, Security, status
supplierXbranch_router = APIRouter()


@supplierXbranch_router.get('/',
    tags=['supplierXbranch'],
    response_model=List[SupplierXBranch],
    description="Returns all supplierXbranch ")
def get_all_supplierXbranchs(credentials: HTTPAuthorizationCredentials = Security(security)) -> List[SupplierXBranch]:
    db = SessionLocal()
    result = supplierXbranchRepository(db).get_all_supplierXbranchs()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@supplierXbranch_router.get('/{id}',
    tags=['supplierXbranch'],
    response_model=SupplierXBranch,
    description="Returns data of one specific supplierXbranch")
def get_supplierXbranch_by_id(id: int = Path(ge=0, le=5000), credentials: HTTPAuthorizationCredentials = Security(security)) -> SupplierXBranch:
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
def create_supplierXbranch(supplierXbranch: SupplierXBranch, credentials: HTTPAuthorizationCredentials = Security(security)) -> dict:
    db = SessionLocal()
    token = credentials.credentials
    payload = auth_handler.decode_token(token=token)
    supplierXbranch.id_branch = payload.get("user.branch")
    new_supplierXbranch = supplierXbranchRepository(db).create_supplierXbranch(supplierXbranch)
    return JSONResponse(content={
        "message": "The supplierXbranch was successfully created",
        "data": jsonable_encoder(new_supplierXbranch)
    }, status_code=201)

@supplierXbranch_router.put('{id}', tags=['supplierXbranch'],
    response_model=dict,
    description="Update a new supplierXbranch")
def update_supplier(credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)],id:int = Path(ge=1), supplierXbranch: SupplierXBranch = Body()) -> dict:
    db= SessionLocal()
    update_supplierXbranch = supplierXbranchRepository(db).update_supplierXbranch(id,supplierXbranch)
    return JSONResponse(
        content={        
        "message": "The supplierXbranch was successfully updated",        
        "data": jsonable_encoder(update_supplierXbranch)    
        }, 
        status_code=status.HTTP_201_CREATED
    )



@supplierXbranch_router.delete('/{id}',
    tags=['supplierXbranch'],
    response_model=dict,
    description="Removes specific supplierXbranch")
def remove_supplierXbranch(id: int = Path(ge=1), credentials: HTTPAuthorizationCredentials = Security(security)) -> dict:
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