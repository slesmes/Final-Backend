from fastapi import APIRouter
from src.schemas.branch import Branch
from fastapi import FastAPI, Body, Query, Path
from fastapi.responses import HTMLResponse, JSONResponse
from typing import Any, Optional, List
from src.config.database import SessionLocal
from src.models.branch import Branch as branchModel
from fastapi.encoders import jsonable_encoder
from src.repositories.branch import branchRepository
branch_router = APIRouter()


@branch_router.get('/',
    tags=['branch'],
    response_model=List[Branch],
    description="Returns all branch ")
def get_all_branchs() -> List[Branch]:
    db = SessionLocal()
    result = branchRepository(db).get_all_branchs()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@branch_router.get('/{id}',
    tags=['branch'],
    response_model=Branch,
    description="Returns data of one specific branch")
def get_branch_by_id(id: int = Path(ge=0, le=5000)) -> Branch:
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
def create_branch(branch: Branch) -> dict:
    db = SessionLocal()
    new_branch = branchRepository(db).create_branch(branch)
    return JSONResponse(content={
        "message": "The branch was successfully created",
        "data": jsonable_encoder(new_branch)
    }, status_code=201)

@branch_router.delete('/{id}',
    tags=['branch'],
    response_model=dict,
    description="Removes specific branch")
def remove_branch(id: int = Path(ge=1)) -> dict:
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