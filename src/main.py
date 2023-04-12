from fastapi import FastAPI

from src.routers import blog, user

from .database import models
from .database.database_connection import engine

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(blog.router)
app.include_router(user.router)
