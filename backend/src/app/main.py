from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import app.routes.htmx as htmx
import app.routes.react as react

app = FastAPI()

app.include_router(htmx.router)
app.include_router(react.router)

origins = [
    "http://localhost:3000",
    "http://localhost:9000",
    "http://fe-h:9000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

