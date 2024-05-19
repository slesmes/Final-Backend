from fastapi import APIRouter
from src.schemas.company import Company
from fastapi import FastAPI, Body, Query, Path
from fastapi.responses import HTMLResponse, JSONResponse
from typing import Any, Optional, List
from src.config.database import SessionLocal
from src.models.company import Company as companyModel
from fastapi.encoders import jsonable_encoder
from src.repositories.company import companyRepository
company_router = APIRouter()


@company_router.get('/',
    tags=['company'],
    response_model=List[Company],
    description="Returns all company ")
def get_all_countries() -> List[Company]:
    db = SessionLocal()
    result = companyRepository(db).get_all_countries()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@company_router.get('/{id}',
    tags=['company'],
    response_model=Company,
    description="Returns data of one specific company")
def get_company_by_id(id: int = Path(ge=0, le=5000)) -> Company:
    db = SessionLocal()
    element = companyRepository(db).get_company(id)
    if not element:
        return JSONResponse(content={
            "message": "The requested company was not found",
            "data": None
        }, status_code=400)
    
    return JSONResponse(content=jsonable_encoder(element),status_code=200)

@company_router.post('/',
    tags=['company'],
    response_model=dict,
    description="Creates a new company")
def create_company(company: Company) -> dict:
    db = SessionLocal()
    new_company = companyRepository(db).create_company(company)
    return JSONResponse(content={
        "message": "The company was successfully created",
        "data": jsonable_encoder(new_company)
    }, status_code=201)

@company_router.delete('/{id}',
    tags=['company'],
    response_model=dict,
    description="Removes specific company")
def remove_company(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    element = companyRepository(db).get_company(id)
    if not element:
        return JSONResponse(content={
            "message": "The requested company was not found",
            "data": None
        }, status_code=404)
    companyRepository(db).delete_company(id)
    return JSONResponse(content={
        "message": "The company was removed successfully",
        "data": None
    }, status_code=200)