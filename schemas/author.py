from typing import Optional

from sqlmodel import SQLModel


class AuthorBase(SQLModel):
    name: str
    bio: Optional[str] = None


class AuthorCreate(AuthorBase):
    pass


class AuthorResponse(AuthorBase):
    id: int
