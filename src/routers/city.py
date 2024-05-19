from fastapi import APIRouter
from src.schemas.city import City
from fastapi import FastAPI, Body, Query, Path
from fastapi.responses import HTMLResponse, JSONResponse
from typing import Any, Optional, List
from src.config.database import SessionLocal
from src.models.city import City as cityModel
from fastapi.encoders import jsonable_encoder
from src.repositories.city import cityRepository
city_router = APIRouter()


@city_router.get('/',
    tags=['city'],
    response_model=List[City],
    description="Returns all city ")
def get_all_countries() -> List[City]:
    db = SessionLocal()
    result = cityRepository(db).get_all_countries()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@city_router.get('/{id}',
    tags=['city'],
    response_model=City,
    description="Returns data of one specific city")
def get_city_by_id(id: int = Path(ge=0, le=5000)) -> City:
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
def create_city(city: City) -> dict:
    db = SessionLocal()
    new_city = cityRepository(db).create_city(city)
    return JSONResponse(content={
        "message": "The city was successfully created",
        "data": jsonable_encoder(new_city)
    }, status_code=201)

@city_router.delete('/{id}',
    tags=['city'],
    response_model=dict,
    description="Removes specific city")
def remove_city(id: int = Path(ge=1)) -> dict:
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