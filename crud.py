# crud.py
from sqlalchemy.orm import Session
from models import Author, Book
from pydantic import BaseModel

class AuthorCreate(BaseModel):
    name: str

class BookCreate(BaseModel):
    title: str
    author_id: int

def create_author(db: Session, author: AuthorCreate):
    db_author = Author(name=author.name)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

def get_authors(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Author).offset(skip).limit(limit).all()

def create_book(db: Session, book: BookCreate):
    db_book = Book(title=book.title, author_id=book.author_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Book).offset(skip).limit(limit).all()
