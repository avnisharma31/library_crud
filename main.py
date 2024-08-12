# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, Base, get_db
import crud
from models import Author, Book
from pydantic import BaseModel

app = FastAPI()

Base.metadata.create_all(bind=engine)

class AuthorCreate(BaseModel):
    name: str

class BookCreate(BaseModel):
    title: str
    author_id: int

@app.post("/authors/", response_model=AuthorCreate)
def create_author(author: AuthorCreate, db: Session = Depends(get_db)):
    return crud.create_author(db, author)

@app.get("/authors/")
def read_authors(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    authors = crud.get_authors(db, skip=skip, limit=limit)
    return authors

@app.post("/books/", response_model=BookCreate)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)

@app.get("/books/")
def read_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    books = crud.get_books(db, skip=skip, limit=limit)
    return books
