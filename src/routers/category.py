from fastapi import APIRouter
from src.schemas.category import Category
from fastapi import FastAPI, Body, Query, Path
from fastapi.responses import HTMLResponse, JSONResponse
from typing import Annotated, Any, Optional, List
from src.config.database import SessionLocal
from src.models.category import Category as categoryModel
from fastapi.encoders import jsonable_encoder
from src.repositories.category import categoryRepository
from src.auth.has_access import security
from fastapi.security import HTTPAuthorizationCredentials
from fastapi import APIRouter, Body, Depends, Query, Path, Security, status
category_router = APIRouter()


@category_router.get('/',
    tags=['category'],
    response_model=List[Category],
    description="Returns all category ")
def get_all_categorys(credentials: HTTPAuthorizationCredentials = Security(security)) -> List[Category]:
    db = SessionLocal()
    result = categoryRepository(db).get_all_categorys()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@category_router.get('/{id}',
    tags=['category'],
    response_model=Category,
    description="Returns data of one specific category")
def get_category_by_id(id: int = Path(ge=0, le=5000),credentials: HTTPAuthorizationCredentials = Security(security)) -> Category:
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
def create_category(category: Category,credentials: HTTPAuthorizationCredentials = Security(security)) -> dict:
    db = SessionLocal()
    new_category = categoryRepository(db).create_category(category)
    return JSONResponse(content={
        "message": "The category was successfully created",
        "data": jsonable_encoder(new_category)
    }, status_code=201)


@category_router.put('{id}', tags=['category'],
    response_model=dict,
    description="Update a new category")
def update_category(credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)],id:int = Path(ge=1), category: Category = Body()) -> dict:
    db= SessionLocal()
    update_category = categoryRepository(db).update_branch(id,category)
    return JSONResponse(
        content={        
        "message": "The category was successfully updated",        
        "data": jsonable_encoder(update_category)    
        }, 
        status_code=status.HTTP_201_CREATED
    )


@category_router.delete('/{id}',
    tags=['category'],
    response_model=dict,
    description="Removes specific category")
def remove_category(id: int = Path(ge=1),credentials: HTTPAuthorizationCredentials = Security(security)) -> dict:
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
