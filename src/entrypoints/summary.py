from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.database.database_connection import SessionLocal
from src.database.hashing import Hash
from src.database.models import Blogs, Users
from src.entrypoints.schemas.blog import Blog, ShowAllBlogs, ShowOneBlog
from src.entrypoints.schemas.user import ShowOneUser, User

router = APIRouter()


def get_db() -> None:
    """Yields to the database."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post(
    "/blog",
    status_code=status.HTTP_201_CREATED,
    response_model=ShowOneBlog,
    tags=["blogs"],
)
def create_new_blog(blog: Blog, db: Session = Depends(get_db)) -> ShowOneBlog:
    """Creates a new blog."""
    new_blog = Blogs(title=blog.title, body=blog.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.delete(
    "/blog/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["blogs"],
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
    "/blog/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=ShowOneBlog,
    tags=["blogs"],
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
    "/blog",
    status_code=status.HTTP_200_OK,
    response_model=list[ShowAllBlogs],
    tags=["blogs"],
)
def get_all_blogs(db: Session = Depends(get_db)) -> list[ShowAllBlogs]:
    """Get all blogs from database."""
    blogs = db.query(Blogs).all()
    return blogs


@router.get(
    "/blog/{id}",
    status_code=status.HTTP_200_OK,
    response_model=ShowOneBlog,
    tags=["blogs"],
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


@router.post(
    "/user",
    status_code=status.HTTP_201_CREATED,
    response_model=ShowOneUser,
    tags=["users"],
)
def create_new_user(user: User, db: Session = Depends(get_db)) -> ShowOneUser:
    """Creates a new user."""
    hashed_password = Hash.get_bcrypt_hashed_password(user.password)
    new_user = Users(
        name=user.name,
        email=user.email,
        password=hashed_password,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get(
    "/user/{id}",
    status_code=status.HTTP_200_OK,
    response_model=ShowOneUser,
    tags=["users"],
)
def get_unique_user(id: int, db: Session = Depends(get_db)) -> ShowOneUser:
    """Get one blog based on a unique id."""
    user = db.query(Users).filter(Users.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"user with id {id} does not exist",
        )
    return user
