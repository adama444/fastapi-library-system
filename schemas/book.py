from datetime import date
from typing import Optional

from sqlmodel import SQLModel


class BookBase(SQLModel):
    title: str
    description: Optional[str] = None
    genre: Optional[str] = None
    published_date: Optional[date] = None


class BookCreate(BookBase):
    author_id: int


class BookUpdate(BookBase):
    title: Optional[str] = None
    author_id: Optional[int] = None


class BookResponse(BookBase):
    id: int
