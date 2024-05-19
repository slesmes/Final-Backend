from fastapi import APIRouter
from src.schemas.country import Country
from fastapi import FastAPI, Body, Query, Path
from fastapi.responses import HTMLResponse, JSONResponse
from typing import Any, Optional, List
from src.config.database import SessionLocal
from src.models.country import Country as CountryModel
from fastapi.encoders import jsonable_encoder
from src.repositories.country import CountryRepository
country_router = APIRouter()


@country_router.get('/',
    tags=['Country'],
    response_model=List[Country],
    description="Returns all Country ")
def get_all_countries() -> List[Country]:
    db = SessionLocal()
    result = CountryRepository(db).get_all_countries()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@country_router.get('/{id}',
    tags=['Country'],
    response_model=Country,
    description="Returns data of one specific country")
def get_country_by_id(id: int = Path(ge=0, le=5000)) -> Country:
    db = SessionLocal()
    element = CountryRepository(db).get_country(id)
    if not element:
        return JSONResponse(content={
            "message": "The requested country was not found",
            "data": None
        }, status_code=400)
    
    return JSONResponse(content=jsonable_encoder(element),status_code=200)

@country_router.post('/',
    tags=['Country'],
    response_model=dict,
    description="Creates a new country")
def create_country(country: Country) -> dict:
    db = SessionLocal()
    new_country = CountryRepository(db).create_country(country)
    return JSONResponse(content={
        "message": "The country was successfully created",
        "data": jsonable_encoder(new_country)
    }, status_code=201)

@country_router.delete('/{id}',
    tags=['Country'],
    response_model=dict,
    description="Removes specific country")
def remove_country(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    element = CountryRepository(db).get_country(id)
    if not element:
        return JSONResponse(content={
            "message": "The requested country was not found",
            "data": None
        }, status_code=404)
    CountryRepository(db).delete_country(id)
    return JSONResponse(content={
        "message": "The country was removed successfully",
        "data": None
    }, status_code=200)