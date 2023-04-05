from fastapi import FastAPI

from src.entrypoints import summary

app = FastAPI()


app.include_router(summary.router)
