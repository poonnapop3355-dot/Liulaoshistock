from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.crud.book_variant import crud_book_variant
from app.schemas.inventory import BookVariant
from app.core.auth import get_current_user

router = APIRouter()

@router.get("/", response_model=List[BookVariant])
def read_book_variants(q: str = ""):
    """
    Retrieve book variants, optionally filtering by a search query.
    """
    if q:
        # In a real application, you would have a more robust search implementation
        return [variant for variant in crud_book_variant.get_multi() if q.lower() in variant.sku.lower()]
    return crud_book_variant.get_multi()
