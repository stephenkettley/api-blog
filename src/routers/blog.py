from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.database.database_connection import get_db
from src.database.models import Blogs, Users
from src.schemas.blog import Blog, ShowAllBlogs, ShowOneBlog

router = APIRouter(
    prefix="/blog",
    tags=["Blogs"],
)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=ShowOneBlog,
)
def create_new_blog(blog: Blog, db: Session = Depends(get_db)) -> ShowOneBlog:
    """Creates a new blog."""
    user = db.query(Users).filter(Users.id == blog.user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"user with id {blog.user_id} does not exist",
        )

    new_blog = Blogs(title=blog.title, body=blog.body, user_id=blog.user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_unique_blog(id: int, db: Session = Depends(get_db)) -> None:
    """Delete a blog with a unique id."""
    fetched_blog = db.query(Blogs).filter(Blogs.id == id)
    if not fetched_blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"blog with id {id} does not exist for deletion",
        )
    else:
        fetched_blog.delete(synchronize_session=False)
        db.commit()


@router.put(
    "/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=ShowOneBlog,
)
def update_unique_blog(
    id: int,
    blog: Blog,
    db: Session = Depends(get_db),
) -> ShowOneBlog:
    """Update a blog with a unique id."""
    fetched_blog = db.query(Blogs).filter(Blogs.id == id)
    if not fetched_blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"blog with id {id} does not exist for updating",
        )
    else:
        fetched_blog.update({"title": blog.title, "body": blog.body})
        db.commit()
        updated_blog = db.query(Blogs).filter(Blogs.id == id).first()

        return updated_blog


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=list[ShowAllBlogs],
)
def get_all_blogs(db: Session = Depends(get_db)) -> list[ShowAllBlogs]:
    """Get all blogs from database."""
    blogs = db.query(Blogs).all()
    return blogs


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=ShowOneBlog,
)
def get_unique_blog(id: int, db: Session = Depends(get_db)) -> ShowOneBlog:
    """Get one blog based on a unique id."""
    blog = db.query(Blogs).filter(Blogs.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"blog with id {id} does not exist",
        )
    return blog
