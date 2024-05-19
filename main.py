from fastapi import FastAPI, Body, Query, Path
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Any, Optional, List

from src.config.database import Base, engine

Base.metadata.create_all(bind=engine)



app = FastAPI()

app.title = "STOCK MASTER"
app.summary = "API with FastAPI and Python"
app.description = "This is a demostration of API REST using Python"
app.version = "0.0.1"


@app.get('/hello',
    tags=["web"],
    description="Shows an HTML hello world")
def greet():
    return HTMLResponse("<h1>Hello World</h1>")