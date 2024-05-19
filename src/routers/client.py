from fastapi import APIRouter
from src.schemas.client import Client
from fastapi import FastAPI, Body, Query, Path
from fastapi.responses import HTMLResponse, JSONResponse
from typing import Any, Optional, List
from src.config.database import SessionLocal
from src.models.client import Client as clientModel
from fastapi.encoders import jsonable_encoder
from src.repositories.client import clientRepository
client_router = APIRouter()


@client_router.get('/',
    tags=['client'],
    response_model=List[Client],
    description="Returns all client ")
def get_all_clients() -> List[Client]:
    db = SessionLocal()
    result = clientRepository(db).get_all_clients()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@client_router.get('/{id}',
    tags=['client'],
    response_model=Client,
    description="Returns data of one specific client")
def get_client_by_id(id: int = Path(ge=0, le=5000)) -> Client:
    db = SessionLocal()
    element = clientRepository(db).get_client(id)
    if not element:
        return JSONResponse(content={
            "message": "The requested client was not found",
            "data": None
        }, status_code=400)
    
    return JSONResponse(content=jsonable_encoder(element),status_code=200)

@client_router.post('/',
    tags=['client'],
    response_model=dict,
    description="Creates a new client")
def create_client(client: Client) -> dict:
    db = SessionLocal()
    new_client = clientRepository(db).create_client(client)
    return JSONResponse(content={
        "message": "The client was successfully created",
        "data": jsonable_encoder(new_client)
    }, status_code=201)

@client_router.delete('/{id}',
    tags=['client'],
    response_model=dict,
    description="Removes specific client")
def remove_client(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    element = clientRepository(db).get_client(id)
    if not element:
        return JSONResponse(content={
            "message": "The requested client was not found",
            "data": None
        }, status_code=404)
    clientRepository(db).delete_client(id)
    return JSONResponse(content={
        "message": "The client was removed successfully",
        "data": None
    }, status_code=200)