from datetime import date
from typing import Optional, List

from sqlmodel import SQLModel, Field, Relationship


class Author(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    bio: Optional[str]

    books: List['Book'] = Relationship(back_populates='author')


class Book(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: Optional[str]
    genre: Optional[str] = Field(index=True)
    published_date: Optional[date]
    is_available: bool = Field(default=True)

    author_id: Optional[int] = Field(default=None, foreign_key='author.id')
    author: Optional[Author] = Relationship(back_populates='books')
