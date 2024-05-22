from fastapi import APIRouter
from src.schemas.user import User
from fastapi import FastAPI, Body, Query, Path
from fastapi.responses import HTMLResponse, JSONResponse
from typing import Annotated, Any, Optional, List
from src.config.database import SessionLocal
from src.models.user import User as userModel
from fastapi.encoders import jsonable_encoder
from src.repositories.user import UserRepository
from src.auth.has_access import security
from src.auth import auth_handler
from fastapi.security import HTTPAuthorizationCredentials
from fastapi import APIRouter, Body, Depends, Query, Path, Security, status
user_router = APIRouter()


@user_router.get('/',
    tags=['user'],
    response_model=List[User],
    description="Returns all user ")
def get_all_users(credentials: HTTPAuthorizationCredentials = Security(security)) -> List[User]:
    db = SessionLocal()
    token = credentials.credentials
    payload = auth_handler.decode_token(token=token)
    branch = payload.get("user.branch")
    result = UserRepository(db).get_all_Users(branch)
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@user_router.get('/{id}',
    tags=['user'],
    response_model=User,
    description="Returns data of one specific user")
def get_user_by_id(id: int = Path(ge=0, le=5000),credentials: HTTPAuthorizationCredentials = Security(security)) -> User:
    db = SessionLocal()
    token = credentials.credentials
    payload = auth_handler.decode_token(token=token)
    branch = payload.get("user.branch")
    element = UserRepository(db).get_user(id, branch)
    if not element:
        return JSONResponse(content={
            "message": "The requested user was not found",
            "data": None
        }, status_code=400)
    
    return JSONResponse(content=jsonable_encoder(element),status_code=200)


@user_router.put('{id}', tags=['user'],
    response_model=dict,
    description="Update a new user")
def update_user(credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)],id:int = Path(ge=1), user: User = Body()) -> dict:
    db= SessionLocal()
    update_user = UserRepository(db).update_user(id,user)
    return JSONResponse(
        content={        
        "message": "The user was successfully updated",        
        "data": jsonable_encoder(update_user)    
        }, 
        status_code=status.HTTP_201_CREATED
    )


@user_router.delete('/{id}',
    tags=['user'],
    response_model=dict,
    description="Removes specific user")
def remove_user(id: int = Path(ge=1), credentials: HTTPAuthorizationCredentials = Security(security)) -> dict:
    db = SessionLocal()
    token = credentials.credentials
    payload = auth_handler.decode_token(token=token)
    branch = payload.get("user.branch")
    element = UserRepository(db).get_user(id, branch)
    if not element:
        return JSONResponse(content={
            "message": "The requested user was not found",
            "data": None
        }, status_code=404)
    UserRepository(db).remove_user(id, branch)
    return JSONResponse(content={
        "message": "The user was removed successfully",
        "data": None
    }, status_code=200)