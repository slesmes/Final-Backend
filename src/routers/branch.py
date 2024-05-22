from fastapi import APIRouter
from src.schemas.branch import Branch
from fastapi import FastAPI, Body, Query, Path
from fastapi.responses import HTMLResponse, JSONResponse
from typing import Annotated, Any, Optional, List
from src.config.database import SessionLocal
from src.models.branch import Branch as branchModel
from fastapi.encoders import jsonable_encoder
from src.repositories.branch import branchRepository
from src.auth.has_access import security
from fastapi.security import HTTPAuthorizationCredentials
from fastapi import APIRouter, Body, Depends, Query, Path, Security, status
branch_router = APIRouter()



@branch_router.get('/',
    tags=['branch'],
    response_model=List[Branch],
    description="Returns all branch ")
def get_all_branchs(credentials: HTTPAuthorizationCredentials = Security(security)) -> List[Branch]:
    db = SessionLocal()
    result = branchRepository(db).get_all_branchs()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@branch_router.get('/{id}',
    tags=['branch'],
    response_model=Branch,
    description="Returns data of one specific branch")
def get_branch_by_id(id: int = Path(ge=0, le=5000), credentials: HTTPAuthorizationCredentials = Security(security)) -> Branch:
    db = SessionLocal()
    element = branchRepository(db).get_branch(id)
    if not element:
        return JSONResponse(content={
            "message": "The requested branch was not found",
            "data": None
        }, status_code=400)
    
    return JSONResponse(content=jsonable_encoder(element),status_code=200)

@branch_router.post('/',
    tags=['branch'],
    response_model=dict,
    description="Creates a new branch")
def create_branch(branch: Branch, credentials: HTTPAuthorizationCredentials = Security(security)) -> dict:
    db = SessionLocal()
    new_branch = branchRepository(db).create_branch(branch)
    return JSONResponse(content={
        "message": "The branch was successfully created",
        "data": jsonable_encoder(new_branch)
    }, status_code=201)

@branch_router.put('{id}', tags=['branch'],
    response_model=dict,
    description="Update a new branch")
def update_branch(credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)],id:int = Path(ge=1), branch: Branch = Body()) -> dict:
    db= SessionLocal()
    update_branch = branchRepository(db).update_branch(id,branch)
    return JSONResponse(
        content={        
        "message": "The branch was successfully updated",        
        "data": jsonable_encoder(update_branch)    
        }, 
        status_code=status.HTTP_201_CREATED
    )

@branch_router.delete('/{id}',
    tags=['branch'],
    response_model=dict,
    description="Removes specific branch")
def remove_branch(id: int = Path(ge=1), credentials: HTTPAuthorizationCredentials = Security(security)) -> dict:
    db = SessionLocal()
    element = branchRepository(db).get_branch(id)
    if not element:
        return JSONResponse(content={
            "message": "The requested branch was not found",
            "data": None
        }, status_code=404)
    branchRepository(db).delete_branch(id)
    return JSONResponse(content={
        "message": "The branch was removed successfully",
        "data": None
    }, status_code=200)
