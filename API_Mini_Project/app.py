from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Books API", description="A Simple API to manage books", version="1.0")

class Book(BaseModel):
    id: int
    title: str

books: List[Book] = []

@app.get("/books", response_model=List[Book])
def get_books():
    return books

@app.post("/books", response_model=Book, status_code=201)
def add_book(book: Book):
    books.append(book)
    return book
 