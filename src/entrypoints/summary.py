from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from src.database import models
from src.database.database_connection import SessionLocal
from src.entrypoints.schemas import blog

router = APIRouter()


def get_db() -> None:
    """Yields to the database."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/blog/create", status_code=status.HTTP_201_CREATED)
def create_new_blog(blog: blog.Blog, db: Session = Depends(get_db)):
    """Creates a new blog."""
    new_blog = models.Blogs(title=blog.title, body=blog.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.get("/blog/all", status_code=status.HTTP_200_OK)
def get_all_blogs(db: Session = Depends(get_db)) -> list:
    """Get all blogs from database."""
    blogs = db.query(models.Blogs).all()
    return blogs


@router.get("/blog/{id}", status_code=status.HTTP_200_OK)
def get_unique_blog(id: int, response: Response, db: Session = Depends(get_db)):
    """Get one blog based on a unique id."""
    blog = db.query(models.Blogs).filter(models.Blogs.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"blog with id {id} does not exist",
        )
    return blog
