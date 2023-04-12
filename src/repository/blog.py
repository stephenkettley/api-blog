from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from src.database.models import Blogs, Users
from src.schemas.blog import Blog, ShowAllBlogs, ShowOneBlog


def get_all(db: Session) -> list[ShowAllBlogs]:
    """Get all blogs."""
    blogs = db.query(Blogs).all()
    return blogs


def create(blog: Blog, db: Session) -> ShowOneBlog:
    """Create new blog."""
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


def delete(id: int, db: Session) -> None:
    """Delete a blog with unique id."""
    fetched_blog = db.query(Blogs).filter(Blogs.id == id)
    if not fetched_blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"blog with id {id} does not exist for deletion",
        )
    else:
        fetched_blog.delete(synchronize_session=False)
        db.commit()


def update(id: int, blog: Blog, db: Session) -> ShowOneBlog:
    """Update a blog with unique id."""
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


def get_unique(id: int, db: Session) -> ShowOneBlog:
    """Get blog with unique id."""
    blog = db.query(Blogs).filter(Blogs.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"blog with id {id} does not exist",
        )
    return blog
