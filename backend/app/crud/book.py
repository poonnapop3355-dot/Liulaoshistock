from app.crud.base import CRUDBase
from app.schemas.book import Book, Author

crud_book = CRUDBase(Book, "/books")
crud_author = CRUDBase(Author, "/authors")
