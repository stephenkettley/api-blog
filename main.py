from typing import Optional

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/blog/all")
def get_all_blogs(
    limit: int = 10, published: bool = True, sort: Optional[str] = None
) -> dict:
    """Get all blogs."""
    if published:
        return {"data": f"list of {limit} published blogs"}
    else:
        return {"data": f"list of {limit} blogs"}


@app.get("/blog/unpublished")
def get_all_unpublished_blogs() -> dict:
    """Get all unpublished blogs."""
    return {"data": "list of all unpublished blogs"}


@app.get("/blog/{id}")
def get_one_blog(id: int) -> dict:
    """Get a blog with specific id."""
    return {"data": f"blog with id {id}"}


@app.get("/blog/{id}/comments")
def show_blog_comments(id: int, limit: int = 10) -> dict:
    """Show comments of blog with specific id."""
    return {"data": f"{limit} comments from blog with id {id}"}


class Blog(BaseModel):
    """Validation class for blog request body."""

    title: str
    body: str
    published: Optional[bool] = False


@app.post("/blog")
def create_blog(blog: Blog) -> dict:
    """Create a new blog."""
    return {
        "message": "new blog has been created",
        "data": {
            "title": blog.title,
            "body": blog.body,
            "published": blog.published,
        },
    }


if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, reload=True, access_log=False)
