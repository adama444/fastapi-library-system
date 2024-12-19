from fastapi import APIRouter, Depends
from sqlmodel import Session

from database import get_session
from schemas.book import BookCreate, BookResponse, BookUpdate
from services.book_service import BookService

router = APIRouter()


@router.post("/", response_model=BookResponse)
def create_book(book: BookCreate, db: Session = Depends(get_session)):
    return BookService.create_book(book, db)


@router.get("/", response_model=list[BookResponse])
def list_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_session)):
    return BookService.list_books(skip, limit, db)


@router.get("/{book_id}", response_model=BookResponse)
def get_book(book_id: int, db: Session = Depends(get_session)):
    return BookService.get_book(book_id, db)


@router.put("/{book_id}", response_model=BookResponse)
def update_book(book_id: int, book: BookUpdate, db: Session = Depends(get_session)):
    return BookService.update_book(book_id, book, db)


@router.delete("/{book_id}", response_model=BookResponse)
def delete_book(book_id: int, db: Session = Depends(get_session)):
    return BookService.delete_book(book_id, db)
