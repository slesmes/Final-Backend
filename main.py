from fastapi import FastAPI, Body, Query, Path
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Any, Optional, List

from src.middlewares.error_handler import ErrorHandler
from src.config.database import Base, engine
from src.routers.country import country_router
from src.routers.department import department_router
from src.routers.city import city_router
from src.routers.company import company_router

Base.metadata.create_all(bind=engine)

tags_metadata = [
    {
        "name": "country",
        "description": "country handling endpoints",
    },
    {
        "name": "user",
        "description": "User handling endpoints",
    },
    {
        "name": "auth",
        "description": "User's authentication",
    },
    {
        "name": "department",
        "description": "department handling endpoints",
    },
    {
        "name": "city",
        "description": "city handling endpoints",
    },
    {
        "name": "company",
        "description": "company handling endpoints",
    }
]
app = FastAPI(openapi_tags=tags_metadata)

app.include_router(prefix="/api/v1/country", router=country_router)
app.include_router(prefix="/api/v1/department", router=department_router)
app.include_router(prefix="/api/v1/city", router=city_router)
app.include_router(prefix="/api/v1/company", router=company_router)

app.add_middleware(ErrorHandler)

app.title = "STOCK MASTER"
app.summary = "API with FastAPI and Python"
app.description = "This is a demostration of API REST using Python"
app.version = "0.0.1"


@app.get('/hello',
    tags=["web"],
    description="Shows an HTML hello world")
def greet():
    return HTMLResponse("<h1>Hello World</h1>")