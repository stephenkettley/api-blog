from fastapi import FastAPI

from src.database import models
from src.database.database_connection import engine
from src.routers import authentication, blog, user

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
