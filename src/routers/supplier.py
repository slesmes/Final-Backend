from fastapi import APIRouter
from src.schemas.supplier import Supplier
from fastapi import FastAPI, Body, Query, Path
from fastapi.responses import HTMLResponse, JSONResponse
from typing import Annotated, Any, Optional, List
from src.config.database import SessionLocal
from src.models.supplier import Supplier as supplierModel
from fastapi.encoders import jsonable_encoder
from src.repositories.supplier import supplierRepository
from src.auth.has_access import security
from fastapi.security import HTTPAuthorizationCredentials
from fastapi import APIRouter, Body, Depends, Query, Path, Security, status
supplier_router = APIRouter()


@supplier_router.get('/',
    tags=['supplier'],
    response_model=List[Supplier],
    description="Returns all supplier ")
def get_all_suppliers(credentials: HTTPAuthorizationCredentials = Security(security)) -> List[Supplier]:
    db = SessionLocal()
    result = supplierRepository(db).get_all_suppliers()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@supplier_router.get('/{id}',
    tags=['supplier'],
    response_model=Supplier,
    description="Returns data of one specific supplier")
def get_supplier_by_id(id: int = Path(ge=0, le=5000),credentials: HTTPAuthorizationCredentials = Security(security)) -> Supplier:
    db = SessionLocal()
    element = supplierRepository(db).get_supplier(id)
    if not element:
        return JSONResponse(content={
            "message": "The requested supplier was not found",
            "data": None
        }, status_code=400)
    
    return JSONResponse(content=jsonable_encoder(element),status_code=200)

@supplier_router.post('/',
    tags=['supplier'],
    response_model=dict,
    description="Creates a new supplier")
def create_supplier(supplier: Supplier, credentials: HTTPAuthorizationCredentials = Security(security)) -> dict:
    db = SessionLocal()
    new_supplier = supplierRepository(db).create_supplier(supplier)
    return JSONResponse(content={
        "message": "The supplier was successfully created",
        "data": jsonable_encoder(new_supplier)
    }, status_code=201)


@supplier_router.put('{id}', tags=['supplier'],
    response_model=dict,
    description="Update a new sale")
def update_supplier(credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)],id:int = Path(ge=1), supplier: Supplier = Body()) -> dict:
    db= SessionLocal()
    update_supplier = supplierRepository(db).update_supplier(id,supplier)
    return JSONResponse(
        content={        
        "message": "The supplier was successfully updated",        
        "data": jsonable_encoder(update_supplier)    
        }, 
        status_code=status.HTTP_201_CREATED
    )


@supplier_router.delete('/{id}',
    tags=['supplier'],
    response_model=dict,
    description="Removes specific supplier")
def remove_supplier(id: int = Path(ge=1), credentials: HTTPAuthorizationCredentials = Security(security)) -> dict:
    db = SessionLocal()
    element = supplierRepository(db).get_supplier(id)
    if not element:
        return JSONResponse(content={
            "message": "The requested supplier was not found",
            "data": None
        }, status_code=404)
    supplierRepository(db).delete_supplier(id)
    return JSONResponse(content={
        "message": "The supplier was removed successfully",
        "data": None
    }, status_code=200)