from fastapi import HTTPException
from sqlmodel import Session, select

from models.book import Author
from schemas.author import AuthorCreate, AuthorBase


class AuthorService:
    @staticmethod
    def create_author(author_data: AuthorCreate, db: Session):
        statement = select(Author).where(Author.name == author_data.name)
        existing_author = db.exec(statement).first()
        if existing_author:
            raise HTTPException(status_code=400, detail="Author with this name already exists")

        new_author = Author(**author_data.model_dump())
        db.add(new_author)
        db.commit()
        db.refresh(new_author)
        return new_author

    @staticmethod
    def list_authors(skip: int, limit: int, db: Session):
        statement = select(Author).offset(skip).limit(limit)
        return db.exec(statement).all()

    @staticmethod
    def get_author(author_id: int, db: Session):
        statement = select(Author).where(Author.id == author_id)
        author = db.exec(statement).first()
        if not author:
            raise HTTPException(status_code=404, detail="Author not found")
        return author

    @staticmethod
    def update_author(author_id: int, author_data: AuthorBase, db: Session):
        statement = select(Author).where(Author.id == author_id)
        author = db.exec(statement).first()
        if not author:
            raise HTTPException(status_code=404, detail="Author not found")

        for field, value in author_data.model_dump(exclude_unset=True).items():
            setattr(author, field, value)

        db.commit()
        db.refresh(author)
        return author

    @staticmethod
    def delete_author(author_id: int, db: Session):
        statement = select(Author).where(Author.id == author_id)
        author = db.exec(statement).first()
        if not author:
            raise HTTPException(status_code=404, detail="Author not found")

        db.delete(author)
        db.commit()
        return author