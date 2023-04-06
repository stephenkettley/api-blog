from sqlalchemy import Column, Integer, String

from .database_connection import Base


class Blogs(Base):
    """Blog object for database relation."""

    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
