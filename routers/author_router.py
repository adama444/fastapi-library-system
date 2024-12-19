from typing import List

from fastapi import APIRouter, Depends
from sqlmodel import Session

from database import get_session
from schemas.author import AuthorResponse, AuthorCreate, AuthorBase
from services.author_service import AuthorService

router = APIRouter()


@router.post("/", response_model=AuthorResponse, status_code=201)
def create_author(author_data: AuthorCreate, db: Session = Depends(get_session)):
    return AuthorService.create_author(author_data, db)


@router.get("/", response_model=List[AuthorResponse])
def list_authors(skip: int = 0, limit: int = 10, db: Session = Depends(get_session)):
    return AuthorService.list_authors(skip, limit, db)


@router.get("/{author_id}", response_model=AuthorResponse)
def get_author(author_id: int, db: Session = Depends(get_session)):
    return AuthorService.get_author(author_id, db)


@router.put("/{author_id}", response_model=AuthorResponse)
def update_author(author_id: int, author_data: AuthorBase, db: Session = Depends(get_session)):
    return AuthorService.update_author(author_id, author_data, db)


@router.delete("/{author_id}", response_model=AuthorResponse)
def delete_author(author_id: int, db: Session = Depends(get_session)):
    return AuthorService.delete_author(author_id, db)
