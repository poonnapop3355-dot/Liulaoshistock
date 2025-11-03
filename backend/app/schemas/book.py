from pydantic import BaseModel
from typing import List, Optional

class Author(BaseModel):
    id: str
    name: str

class Book(BaseModel):
    id: str
    isbn10: Optional[str]
    isbn13: str
    title_th: str
    title_en: Optional[str]
    language: str
    authors: List[str]  # List of author IDs
    publisher: Optional[str]
    edition: Optional[str]
    binding: Optional[str]
    pages: Optional[int]
    dimensions: Optional[str]
    weight_g: Optional[int]
    description: Optional[str]
