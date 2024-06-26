from fastapi import APIRouter
from src.schemas.department import Department
from fastapi import FastAPI, Body, Query, Path
from fastapi.responses import HTMLResponse, JSONResponse
from typing import Annotated, Any, Optional, List
from src.config.database import SessionLocal
from src.models.department import Department as departmentModel
from fastapi.encoders import jsonable_encoder
from src.repositories.department import DepartmentRepository
from src.auth.has_access import security
from fastapi.security import HTTPAuthorizationCredentials
from fastapi import APIRouter, Body, Depends, Query, Path, Security, status
department_router = APIRouter()


@department_router.get('/',
    tags=['department'],
    response_model=List[Department],
    description="Returns all department ")
def get_all_departments(credentials: HTTPAuthorizationCredentials = Security(security)) -> List[Department]:
    db = SessionLocal()
    result = DepartmentRepository(db).get_all_departments()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@department_router.get('/{id}',
    tags=['department'],
    response_model=Department,
    description="Returns data of one specific department")
def get_department_by_id(id: int = Path(ge=0, le=5000), credentials: HTTPAuthorizationCredentials = Security(security)) -> Department:
    db = SessionLocal()
    element = DepartmentRepository(db).get_department(id)
    if not element:
        return JSONResponse(content={
            "message": "The requested department was not found",
            "data": None
        }, status_code=400)
    
    return JSONResponse(content=jsonable_encoder(element),status_code=200)

@department_router.post('/',
    tags=['department'],
    response_model=dict,
    description="Creates a new department")
def create_department(department: Department, credentials: HTTPAuthorizationCredentials = Security(security)) -> dict:
    db = SessionLocal()
    new_department = DepartmentRepository(db).create_department(department)
    return JSONResponse(content={
        "message": "The department was successfully created",
        "data": jsonable_encoder(new_department)
    }, status_code=201)

@department_router.put('{id}', tags=['department'],
    response_model=dict,
    description="Update a new department")
def update_country(credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)],id:int = Path(ge=1), department: Department = Body()) -> dict:
    db= SessionLocal()
    update_department = DepartmentRepository(db).update_department(id,department)
    return JSONResponse(
        content={        
        "message": "The department was successfully updated",        
        "data": jsonable_encoder(update_department)    
        }, 
        status_code=status.HTTP_201_CREATED
    )



@department_router.delete('/{id}',
    tags=['department'],
    response_model=dict,
    description="Removes specific department")
def remove_department(id: int = Path(ge=1), credentials: HTTPAuthorizationCredentials = Security(security)) -> dict:
    db = SessionLocal()
    element = DepartmentRepository(db).get_department(id)
    if not element:
        return JSONResponse(content={
            "message": "The requested department was not found",
            "data": None
        }, status_code=404)
    DepartmentRepository(db).delete_department(id)
    return JSONResponse(content={
        "message": "The department was removed successfully",
        "data": None
    }, status_code=200)