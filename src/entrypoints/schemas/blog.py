from pydantic import BaseModel


class Blog(BaseModel):
    """Structure of a blog."""

    title: str
    body: str
