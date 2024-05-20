from fastapi import APIRouter
from src.schemas.part import Part
from fastapi import FastAPI, Body, Query, Path
from fastapi.responses import HTMLResponse, JSONResponse
from typing import Any, Optional, List
from src.config.database import SessionLocal
from src.models.part import Part as partModel
from fastapi.encoders import jsonable_encoder
from src.repositories.part import partRepository
part_router = APIRouter()


@part_router.get('/',
    tags=['part'],
    response_model=List[Part],
    description="Returns all part ")
def get_all_parts() -> List[Part]:
    db = SessionLocal()
    result = partRepository(db).get_all_parts()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@part_router.get('/{id}',
    tags=['part'],
    response_model=Part,
    description="Returns data of one specific part")
def get_part_by_id(id: int = Path(ge=0, le=5000)) -> Part:
    db = SessionLocal()
    element = partRepository(db).get_part(id)
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
def create_part(part: Part) -> dict:
    db = SessionLocal()
    new_part = partRepository(db).create_part(part)
    return JSONResponse(content={
        "message": "The part was successfully created",
        "data": jsonable_encoder(new_part)
    }, status_code=201)

@part_router.delete('/{id}',
    tags=['part'],
    response_model=dict,
    description="Removes specific part")
def remove_part(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    element = partRepository(db).get_part(id)
    if not element:
        return JSONResponse(content={
            "message": "The requested part was not found",
            "data": None
        }, status_code=404)
    partRepository(db).delete_part(id)
    return JSONResponse(content={
        "message": "The part was removed successfully",
        "data": None
    }, status_code=200)