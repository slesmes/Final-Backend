from fastapi import APIRouter
from src.schemas.rol import Rol
from fastapi import FastAPI, Body, Query, Path
from fastapi.responses import HTMLResponse, JSONResponse
from typing import Annotated, Any, Optional, List
from src.config.database import SessionLocal
from src.models.rol import Rol as rolModel
from fastapi.encoders import jsonable_encoder
from src.repositories.rol import rolRepository
from src.auth.has_access import security
from fastapi.security import HTTPAuthorizationCredentials
from fastapi import APIRouter, Body, Depends, Query, Path, Security, status
rol_router = APIRouter()


@rol_router.get('/',
    tags=['rol'],
    response_model=List[Rol],
    description="Returns all rol ")
def get_all_rols(credentials: HTTPAuthorizationCredentials = Security(security)) -> List[Rol]:
    db = SessionLocal()
    result = rolRepository(db).get_all_rols()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@rol_router.get('/{id}',
    tags=['rol'],
    response_model=Rol,
    description="Returns data of one specific rol")
def get_rol_by_id(id: int = Path(ge=0, le=5000), credentials: HTTPAuthorizationCredentials = Security(security)) -> Rol:
    db = SessionLocal()
    element = rolRepository(db).get_rol(id)
    if not element:
        return JSONResponse(content={
            "message": "The requested rol was not found",
            "data": None
        }, status_code=400)
    
    return JSONResponse(content=jsonable_encoder(element),status_code=200)

@rol_router.post('/',
    tags=['rol'],
    response_model=dict,
    description="Creates a new rol")
def create_rol(rol: Rol, credentials: HTTPAuthorizationCredentials = Security(security)) -> dict:
    db = SessionLocal()
    new_rol = rolRepository(db).create_rol(rol)
    return JSONResponse(content={
        "message": "The rol was successfully created",
        "data": jsonable_encoder(new_rol)
    }, status_code=201)

@rol_router.put('{id}', tags=['rol'],
    response_model=dict,
    description="Update a new rol")
def update_rol(credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)],id:int = Path(ge=1), rol: Rol = Body()) -> dict:
    db= SessionLocal()
    update_rol = rolRepository(db).update_rol(id,rol)
    return JSONResponse(
        content={        
        "message": "The rol was successfully updated",        
        "data": jsonable_encoder(update_rol)    
        }, 
        status_code=status.HTTP_201_CREATED
    )



@rol_router.delete('/{id}',
    tags=['rol'],
    response_model=dict,
    description="Removes specific rol")
def remove_rol(id: int = Path(ge=1), credentials: HTTPAuthorizationCredentials = Security(security)) -> dict:
    db = SessionLocal()
    element = rolRepository(db).get_rol(id)
    if not element:
        return JSONResponse(content={
            "message": "The requested rol was not found",
            "data": None
        }, status_code=404)
    rolRepository(db).delete_rol(id)
    return JSONResponse(content={
        "message": "The rol was removed successfully",
        "data": None
    }, status_code=200)