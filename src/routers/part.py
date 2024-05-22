from fastapi import APIRouter
from src.schemas.part import Part
from fastapi import FastAPI, Body, Query, Path
from fastapi.responses import HTMLResponse, JSONResponse
from typing import Annotated, Any, Optional, List
from src.config.database import SessionLocal
from src.models.part import Part as partModel
from fastapi.encoders import jsonable_encoder
from src.repositories.part import partRepository
from src.auth.has_access import security
from src.auth import auth_handler
from fastapi.security import HTTPAuthorizationCredentials
from fastapi import APIRouter, Body, Depends, Query, Path, Security, status
part_router = APIRouter()


@part_router.get('/',
    tags=['part'],
    response_model=List[Part],
    description="Returns all part ")
def get_all_parts(credentials: HTTPAuthorizationCredentials = Security(security)) -> List[Part]:
    db = SessionLocal()
    token = credentials.credentials
    payload = auth_handler.decode_token(token=token)
    branch = payload.get("user.branch")
    result = partRepository(db).get_all_parts(branch)
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@part_router.get('/{id}',
    tags=['part'],
    response_model=Part,
    description="Returns data of one specific part")
def get_part_by_id(id: int = Path(ge=0, le=5000), credentials: HTTPAuthorizationCredentials = Security(security)) -> Part:
    db = SessionLocal()
    token = credentials.credentials
    payload = auth_handler.decode_token(token=token)
    branch = payload.get("user.branch")
    element = partRepository(db).get_part(id, branch)
    if not element:
        return JSONResponse(content={
            "message": "The requested part was not found",
            "data": None
        }, status_code=400)
    
    return JSONResponse(content=jsonable_encoder(element),status_code=200)

@part_router.post('/',
    tags=['part'],
    response_model=dict,
    description="Creates a new part")
def create_part(part: Part, credentials: HTTPAuthorizationCredentials = Security(security)) -> dict:
    db = SessionLocal()
    new_part = partRepository(db).create_part(part)
    return JSONResponse(content={
        "message": "The part was successfully created",
        "data": jsonable_encoder(new_part)
    }, status_code=201)


@part_router.put('{id}', tags=['part'],
    response_model=dict,
    description="Update a new part")
def update_part(credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)],id:int = Path(ge=1), part: Part = Body()) -> dict:
    db= SessionLocal()
    update_part = partRepository(db).update_part(id,part)
    return JSONResponse(
        content={        
        "message": "The part was successfully updated",        
        "data": jsonable_encoder(update_part)    
        }, 
        status_code=status.HTTP_201_CREATED
    )


@part_router.delete('/{id}',
    tags=['part'],
    response_model=dict,
    description="Removes specific part")
def remove_part(id: int = Path(ge=1), credentials: HTTPAuthorizationCredentials = Security(security)) -> dict:
    db = SessionLocal()
    token = credentials.credentials
    payload = auth_handler.decode_token(token=token)
    branch = payload.get("user.branch")
    element = partRepository(db).get_part(id, branch)
    if not element:
        return JSONResponse(content={
            "message": "The requested part was not found",
            "data": None
        }, status_code=404)
    partRepository(db).delete_part(id, branch)
    return JSONResponse(content={
        "message": "The part was removed successfully",
        "data": None
    }, status_code=200)