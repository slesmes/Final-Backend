from fastapi import APIRouter
from src.schemas.country import Country
from fastapi import FastAPI, Body, Query, Path
from fastapi.responses import HTMLResponse, JSONResponse
from typing import Annotated, Any, Optional, List
from src.config.database import SessionLocal
from src.models.country import Country as CountryModel
from fastapi.encoders import jsonable_encoder
from src.repositories.country import CountryRepository
from src.auth.has_access import security
from fastapi.security import HTTPAuthorizationCredentials
from fastapi import APIRouter, Body, Depends, Query, Path, Security, status
country_router = APIRouter()


@country_router.get('/',
    tags=['country'],
    response_model=List[Country],
    description="Returns all Country ")
def get_all_countries(credentials: HTTPAuthorizationCredentials = Security(security)) -> List[Country]:
    db = SessionLocal()
    result = CountryRepository(db).get_all_countries()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@country_router.get('/{id}',
    tags=['country'],
    response_model=Country,
    description="Returns data of one specific country")
def get_country_by_id(id: int = Path(ge=0, le=5000),credentials: HTTPAuthorizationCredentials = Security(security)) -> Country:
    db = SessionLocal()
    element = CountryRepository(db).get_country(id)
    if not element:
        return JSONResponse(content={
            "message": "The requested country was not found",
            "data": None
        }, status_code=400)
    
    return JSONResponse(content=jsonable_encoder(element),status_code=200)

@country_router.post('/',
    tags=['country'],
    response_model=dict,
    description="Creates a new country")
def create_country(country: Country, credentials: HTTPAuthorizationCredentials = Security(security)) -> dict:
    db = SessionLocal()
    new_country = CountryRepository(db).create_country(country)
    return JSONResponse(content={
        "message": "The country was successfully created",
        "data": jsonable_encoder(new_country)
    }, status_code=201)

@country_router.put('{id}', tags=['country'],
    response_model=dict,
    description="Update a new country")
def update_country(credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)],id:int = Path(ge=1), country: Country = Body()) -> dict:
    db= SessionLocal()
    update_country = CountryRepository(db).update_country(id,country)
    return JSONResponse(
        content={        
        "message": "The country was successfully updated",        
        "data": jsonable_encoder(update_country)    
        }, 
        status_code=status.HTTP_201_CREATED
    )


@country_router.delete('/{id}',
    tags=['country'],
    response_model=dict,
    description="Removes specific country")
def remove_country(id: int = Path(ge=1), credentials: HTTPAuthorizationCredentials = Security(security)) -> dict:
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