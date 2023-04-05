from fastapi import APIRouter

from src.entrypoints.schemas.schemas import Blog

router = APIRouter()


@router.post("/blog/create")
def create_new_blog(blog: Blog) -> dict:
    return {
        "new blog created": {
            "title": blog.title,
            "body": blog.body,
            "published": blog.published,
        }
    }
