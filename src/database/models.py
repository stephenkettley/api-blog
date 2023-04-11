from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database_connection import Base


class Blogs(Base):
    """Blog object for database relation."""

    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    creator = relationship("Users", back_populates="blogs")


class Users(Base):
    """Blog object for database relation."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    blogs = relationship("Blogs", back_populates="creator")
