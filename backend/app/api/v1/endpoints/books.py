from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.crud.book import crud_book
from app.schemas.book import Book
from app.core.auth import get_current_user
from app.core.rbac import require_role

router = APIRouter()

@router.post("/", response_model=Book, dependencies=[Depends(require_role(["admin", "manager"]))])
def create_book(book: Book):
    return crud_book.create(book)

@router.get("/", response_model=List[Book])
def read_books():
    return crud_book.get_multi()

@router.get("/{book_id}", response_model=Book)
def read_book(book_id: str):
    db_book = crud_book.get(book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@router.put("/{book_id}", response_model=Book, dependencies=[Depends(require_role(["admin", "manager"]))])
def update_book(book_id: str, book: Book):
    return crud_book.update(book_id, book.dict())

@router.delete("/{book_id}", response_model=Book, dependencies=[Depends(require_role(["admin"]))])
def delete_book(book_id: str):
    db_book = crud_book.get(book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    crud_book.remove(book_id)
    return db_book
