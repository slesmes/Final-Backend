from fastapi import APIRouter
from src.schemas.user import User
from fastapi import FastAPI, Body, Query, Path
from fastapi.responses import HTMLResponse, JSONResponse
from typing import Any, Optional, List
from src.config.database import SessionLocal
from src.models.user import User as userModel
from fastapi.encoders import jsonable_encoder
from src.repositories.user import UserRepository
user_router = APIRouter()


@user_router.get('/',
    tags=['user'],
    response_model=List[User],
    description="Returns all user ")
def get_all_users() -> List[User]:
    db = SessionLocal()
    result = UserRepository(db).get_all_Users()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@user_router.get('/{id}',
    tags=['user'],
    response_model=User,
    description="Returns data of one specific user")
def get_user_by_id(id: int = Path(ge=0, le=5000)) -> User:
    db = SessionLocal()
    element = UserRepository(db).get_user(id)
    if not element:
        return JSONResponse(content={
            "message": "The requested user was not found",
            "data": None
        }, status_code=400)
    
    return JSONResponse(content=jsonable_encoder(element),status_code=200)

@user_router.post('/',
    tags=['user'],
    response_model=dict,
    description="Creates a new user")
def create_user(user: User) -> dict:
    db = SessionLocal()
    new_user = UserRepository(db).create_User(user)
    return JSONResponse(content={
        "message": "The user was successfully created",
        "data": jsonable_encoder(new_user)
    }, status_code=201)

@user_router.delete('/{id}',
    tags=['user'],
    response_model=dict,
    description="Removes specific user")
def remove_user(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    element = UserRepository(db).get_user(id)
    if not element:
        return JSONResponse(content={
            "message": "The requested user was not found",
            "data": None
        }, status_code=404)
    UserRepository(db).remove_user(id)
    return JSONResponse(content={
        "message": "The user was removed successfully",
        "data": None
    }, status_code=200)