import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index() -> dict:
    return {
        "data": {
            "name": "Stephen",
            "age": 25,
        }
    }


@app.get("/about")
def about() -> dict:
    return {"data": "about page"}


if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, reload=True, access_log=False)
