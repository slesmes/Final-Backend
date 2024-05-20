from fastapi import APIRouter
from src.schemas.category import Category
from fastapi import FastAPI, Body, Query, Path
from fastapi.responses import HTMLResponse, JSONResponse
from typing import Any, Optional, List
from src.config.database import SessionLocal
from src.models.category import Category as categoryModel
from fastapi.encoders import jsonable_encoder
from src.repositories.category import categoryRepository
category_router = APIRouter()


@category_router.get('/',
    tags=['category'],
    response_model=List[Category],
    description="Returns all category ")
def get_all_categorys() -> List[Category]:
    db = SessionLocal()
    result = categoryRepository(db).get_all_categorys()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@category_router.get('/{id}',
    tags=['category'],
    response_model=Category,
    description="Returns data of one specific category")
def get_category_by_id(id: int = Path(ge=0, le=5000)) -> Category:
    db = SessionLocal()
    element = categoryRepository(db).get_category(id)
    if not element:
        return JSONResponse(content={
            "message": "The requested category was not found",
            "data": None
        }, status_code=400)
    
    return JSONResponse(content=jsonable_encoder(element),status_code=200)

@category_router.post('/',
    tags=['category'],
    response_model=dict,
    description="Creates a new category")
def create_category(category: Category) -> dict:
    db = SessionLocal()
    new_category = categoryRepository(db).create_category(category)
    return JSONResponse(content={
        "message": "The category was successfully created",
        "data": jsonable_encoder(new_category)
    }, status_code=201)

@category_router.delete('/{id}',
    tags=['category'],
    response_model=dict,
    description="Removes specific category")
def remove_category(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    element = categoryRepository(db).get_category(id)
    if not element:
        return JSONResponse(content={
            "message": "The requested category was not found",
            "data": None
        }, status_code=404)
    categoryRepository(db).delete_category(id)
    return JSONResponse(content={
        "message": "The category was removed successfully",
        "data": None
    }, status_code=200)

@category_router.put('/{id}',
    tags=['category'],
    response_model=dict,
    description="Updates specific category")
def update_category(id: int , category: Category = Body()) -> dict:
    db = SessionLocal()
    element = categoryRepository(db).get_category(id)
    if not element:
        return JSONResponse(content={
            "message": "The requested category  was not found",
            "data": None
        }, status_code=404)
    
    element = categoryRepository(db).update_category(id,category)
    return JSONResponse(content={
    "message": "The category was successfully updated",
    "data": jsonable_encoder(element)
    }, status_code=200)