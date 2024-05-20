from fastapi import APIRouter
from src.schemas.city import City
from fastapi import FastAPI, Body, Query, Path
from fastapi.responses import HTMLResponse, JSONResponse
from typing import Annotated, Any, Optional, List
from src.config.database import SessionLocal
from src.models.city import City as cityModel
from fastapi.encoders import jsonable_encoder
from src.repositories.city import cityRepository
from src.auth.has_access import security
from fastapi.security import HTTPAuthorizationCredentials
from fastapi import APIRouter, Body, Depends, Query, Path, Security, status
city_router = APIRouter()


@city_router.get('/',
    tags=['city'],
    response_model=List[City],
    description="Returns all city ")
def get_all_cities(credentials: HTTPAuthorizationCredentials = Security(security)) -> List[City]:
    db = SessionLocal()
    result = cityRepository(db).get_all_cities()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@city_router.get('/{id}',
    tags=['city'],
    response_model=City,
    description="Returns data of one specific city")
def get_city_by_id(id: int = Path(ge=0, le=5000),credentials: HTTPAuthorizationCredentials = Security(security)) -> City:
    db = SessionLocal()
    element = cityRepository(db).get_city(id)
    if not element:
        return JSONResponse(content={
            "message": "The requested city was not found",
            "data": None
        }, status_code=400)
    
    return JSONResponse(content=jsonable_encoder(element),status_code=200)

@city_router.post('/',
    tags=['city'],
    response_model=dict,
    description="Creates a new city")
def create_city(city: City, credentials: HTTPAuthorizationCredentials = Security(security)) -> dict:
    db = SessionLocal()
    new_city = cityRepository(db).create_city(city)
    return JSONResponse(content={
        "message": "The city was successfully created",
        "data": jsonable_encoder(new_city)
    }, status_code=201)


@city_router.put('{id}', tags=['city'],
    response_model=dict,
    description="Update a new category")
def update_city(credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)],id:int = Path(ge=1), city: City = Body()) -> dict:
    db= SessionLocal()
    update_city = cityRepository(db).update_branch(id,city)
    return JSONResponse(
        content={        
        "message": "The city was successfully updated",        
        "data": jsonable_encoder(update_city)    
        }, 
        status_code=status.HTTP_201_CREATED
    )




@city_router.delete('/{id}',
    tags=['city'],
    response_model=dict,
    description="Removes specific city")
def remove_city(id: int = Path(ge=1), credentials: HTTPAuthorizationCredentials = Security(security)) -> dict:
    db = SessionLocal()
    element = cityRepository(db).get_city(id)
    if not element:
        return JSONResponse(content={
            "message": "The requested city was not found",
            "data": None
        }, status_code=404)
    cityRepository(db).delete_city(id)
    return JSONResponse(content={
        "message": "The city was removed successfully",
        "data": None
    }, status_code=200)