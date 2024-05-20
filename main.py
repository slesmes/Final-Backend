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
from src.routers.branch import branch_router
from src.routers.client import client_router
from src.routers.rol import rol_router
from src.routers.user import user_router
from src.routers.bill import bill_router
from src.routers.product import product_router
from src.routers.category import category_router
from src.routers.supplier import supplier_router
from src.routers.productXsupplier import productXsupplier_router
from src.routers.supplierXbranch import supplierXbranch_router
from src.routers.sale import sale_router

Base.metadata.create_all(bind=engine)

tags_metadata = [
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
    },
    {
        "name": "branch",
        "description": "branch handling endpoints",
    },
    {
        "name": "client",
        "description": "client handling endpoints",
    },
    {
        "name": "bill",
        "description": "bill handling endpoints",
    },
    {
        "name": "rol",
        "description": "rol handling endpoints",
    },
    {
        "name": "product",
        "description": "product handling endpoints",
    },
    {
        "name": "category",
        "description": "category handling endpoints",
    },
    {
        "name": "supplier",
        "description": "supplier handling endpoints",
    },
    {
        "name": "ProductXsupplier",
        "description": "ProductXsupplier handling endpoints",
    },
    {
        "name": "supplierXbranch",
        "description": "supplierXbranch handling endpoints",
    },
    {
        "name": "sale",
        "description": "sale handling endpoints",
    }
]
app = FastAPI(openapi_tags=tags_metadata)

app.include_router(prefix="/api/v1/country", router=country_router)
app.include_router(prefix="/api/v1/department", router=department_router)
app.include_router(prefix="/api/v1/city", router=city_router)
app.include_router(prefix="/api/v1/company", router=company_router)
app.include_router(prefix="/api/v1/branch", router=branch_router)
app.include_router(prefix="/api/v1/client", router=client_router)
app.include_router(prefix="/api/v1/rol", router=rol_router)
app.include_router(prefix="/api/v1/user", router=user_router)
app.include_router(prefix="/api/v1/bill", router=bill_router)
app.include_router(prefix="/api/v1/product", router=product_router)
app.include_router(prefix="/api/v1/category", router=category_router)
app.include_router(prefix="/api/v1/supplier", router=supplier_router)
app.include_router(prefix="/api/v1/producdxsupplier", router=productXsupplier_router)
app.include_router(prefix="/api/v1/supplierxbranch", router=supplierXbranch_router)
app.include_router(prefix="/api/v1/sale", router=sale_router)

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