from fastapi import FastAPI

from src.entrypoints import summary

from .database import models
from .database.database_connection import engine

app = FastAPI()

models.Base.metadata.create_all(engine)
app.include_router(summary.router)
