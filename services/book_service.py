from fastapi import HTTPException
from sqlmodel import Session, select

from models.book import Author, Book
from schemas.book import BookCreate, BookUpdate


class BookService:
    @staticmethod
    def create_book(book_data: BookCreate, db: Session):
        statement = select(Author).where(Author.id == book_data.author_id)
        author = db.exec(statement).first()
        if not author:
            raise HTTPException(status_code=404, detail="Author not found")

        new_book = Book(**book_data.model_dump())
        db.add(new_book)
        db.commit()
        db.refresh(new_book)
        return new_book

    @staticmethod
    def list_books(skip: int, limit: int, db: Session):
        statement = select(Book).where(Book.is_available == True).offset(skip).limit(limit)
        return db.exec(statement).all()

    @staticmethod
    def get_book(book_id: int, db: Session):
        statement = select(Book).where(Book.id == book_id).where(Book.is_available == True)
        book = db.exec(statement).first()
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
        return book

    @staticmethod
    def update_book(book_id: int, book_data: BookUpdate, db: Session):
        statement = select(Book).where(Book.id == book_id)
        existing_book = db.exec(statement).first()
        if not existing_book:
            raise HTTPException(status_code=404, detail="Book not found")

        if book_data.author_id:
            statement = select(Author).where(Author.id == book_data.author_id)
            author = db.exec(statement).first()
            if not author:
                raise HTTPException(status_code=404, detail="Author not found")

        for field, value in book_data.model_dump(exclude_unset=True).items():
            setattr(existing_book, field, value)

        db.commit()
        db.refresh(existing_book)
        return existing_book

    @staticmethod
    def delete_book(book_id: int, db: Session):
        statement = select(Book).where(Book.id == book_id)
        book = db.exec(statement).first()

        if not book:
            raise HTTPException(status_code=404, detail="Book not found")

        book.is_active = False
        db.commit()
        return book
