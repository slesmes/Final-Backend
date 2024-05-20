from fastapi import APIRouter
from src.schemas.bill import Bill
from fastapi import FastAPI, Body, Query, Path
from fastapi.responses import HTMLResponse, JSONResponse
from typing import Any, Optional, List
from src.config.database import SessionLocal
from src.models.bill import Bill as billModel
from fastapi.encoders import jsonable_encoder
from src.repositories.bill import billRepository
bill_router = APIRouter()


@bill_router.get('/',
    tags=['bill'],
    response_model=List[Bill],
    description="Returns all bill ")
def get_all_bills() -> List[Bill]:
    db = SessionLocal()
    result = billRepository(db).get_all_bills()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@bill_router.get('/{id}',
    tags=['bill'],
    response_model=Bill,
    description="Returns data of one specific bill")
def get_bill_by_id(id: int = Path(ge=0, le=5000)) -> Bill:
    db = SessionLocal()
    element = billRepository(db).get_bill(id)
    if not element:
        return JSONResponse(content={
            "message": "The requested bill was not found",
            "data": None
        }, status_code=400)
    
    return JSONResponse(content=jsonable_encoder(element),status_code=200)

@bill_router.post('/',
    tags=['bill'],
    response_model=dict,
    description="Creates a new bill")
def create_bill(bill: Bill) -> dict:
    db = SessionLocal()
    new_bill = billRepository(db).create_bill(bill)
    return JSONResponse(content={
        "message": "The bill was successfully created",
        "data": jsonable_encoder(new_bill)
    }, status_code=201)

@bill_router.delete('/{id}',
    tags=['bill'],
    response_model=dict,
    description="Removes specific bill")
def remove_bill(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    element = billRepository(db).get_bill(id)
    if not element:
        return JSONResponse(content={
            "message": "The requested bill was not found",
            "data": None
        }, status_code=404)
    billRepository(db).delete_bill(id)
    return JSONResponse(content={
        "message": "The bill was removed successfully",
        "data": None
    }, status_code=200)

@bill_router.put('/{id}',
    tags=['bill'],
    response_model=dict,
    description="Updates specific bill")
def update_bill(id: int , bill: Bill = Body()) -> dict:
    db = SessionLocal()
    element = billRepository(db).get_bill(id)
    if not element:
        return JSONResponse(content={
            "message": "The requested bill was not found",
            "data": None
        }, status_code=404)
    
    element = billRepository(db).update_bill(id,bill)
    return JSONResponse(content={
    "message": "The bill was successfully updated",
    "data": jsonable_encoder(element)
    }, status_code=200)