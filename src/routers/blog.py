from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.authentication.oauth2 import get_current_user
from src.database.database_connection import get_db
from src.repository.blog import create, delete, get_all, get_unique, update
from src.schemas.blog import Blog, ShowAllBlogs, ShowOneBlog
from src.schemas.user import User

router = APIRouter(
    prefix="/blog",
    tags=["Blogs"],
)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=list[ShowAllBlogs],
)
def get_all_blogs(
    db: Session = Depends(get_db), current_user: User = Depends(get_current_user)
) -> list[ShowAllBlogs]:
    """Get all blogs from database."""
    return get_all(db=db)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=ShowOneBlog,
)
def create_new_blog(
    blog: Blog,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> ShowOneBlog:
    """Create a new blog."""
    return create(
        blog=blog,
        db=db,
    )


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_unique_blog(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> None:
    """Delete a blog with a unique id."""
    delete(
        id=id,
        db=db,
    )


@router.put(
    "/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=ShowOneBlog,
)
def update_unique_blog(
    id: int,
    blog: Blog,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> ShowOneBlog:
    """Update a blog with a unique id."""
    return update(
        id=id,
        blog=blog,
        db=db,
    )


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=ShowOneBlog,
)
def get_unique_blog(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> ShowOneBlog:
    """Get one blog based on a unique id."""
    return get_unique(
        id=id,
        db=db,
    )
