from fastapi import APIRouter, Body, Depends, Query, Path, Security, status
from fastapi.responses import JSONResponse
from typing import Annotated, List
from fastapi.security import HTTPAuthorizationCredentials
from fastapi.encoders import jsonable_encoder
from src.repositories.auth import AuthRepository
from src.config.database import SessionLocal
from src.schemas.user import User as UserCreateSchema
from src.schemas.user import LoginUser as UserLoginSchema
from src.auth.has_access import has_access, security
from src.auth import auth_handler


auth_router = APIRouter()


@auth_router.post(
"/register",
tags=["auth"],
response_model=dict,
description="Register a new user",
)
def register_user(user: UserCreateSchema = Body()) -> dict:
    try:
        print(user)
        new_user = AuthRepository().register_user(user)
        return JSONResponse(
        content={
        "message": "The user was successfully registered",
        "data": jsonable_encoder(new_user),
        },
        status_code=status.HTTP_201_CREATED,
        )
    except Exception as err:
        return JSONResponse(
        content={"message": str(err), "data": None},
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        )
    

@auth_router.post(
"/login",
tags=["auth"],
response_model=dict,
description="Authenticate an user"
)
def login_user(user: UserLoginSchema) -> dict:
    try:
        access_token, refresh_token = AuthRepository().login_user(user)
        return JSONResponse(
        content={"access_token": access_token,
        "refresh_token": refresh_token},
        status_code=status.HTTP_200_OK,
        )
    except Exception as err:
        return JSONResponse(
        content={"message": "Invalid credentials",
        "data": str(err)},
        status_code=status.HTTP_401_UNAUTHORIZED,
        )


@auth_router.get(
"/refresh_token",
tags=["auth"],
response_model=dict,
description="Creates a new token with extended lifetime",
)
def refresh_token(credentials: HTTPAuthorizationCredentials = Security(security)) -> dict:
    refresh_token = credentials.credentials
    new_token = auth_handler.refresh_token(refresh_token)
    return {"access_token": new_token}


@auth_router.get("/notsecret",tags=["auth"],response_model=str,description="Test a NON authentication protected route",)
def not_secret_data() -> str:
    return "Not secret data"

@auth_router.post(
"/secret",
tags=["auth"],
response_model=str,
description="Test authentication protected route",
)
def secret_data(credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)]) -> str:
    token = credentials.credentials
    payload = auth_handler.decode_token(token=token)
    if payload:
        current_user = payload.get("sub")
        return f"Top Secret data only authorized users can access this info:{current_user}"



@auth_router.get(
"/endpoint",
tags=["test"],
response_model=str,
description="...",
)
def test_endpoint(
credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)]
) -> str:
    token = credentials.credentials
    payload = auth_handler.decode_token(token=token)
    if payload:
        issue = payload.get("xxx")