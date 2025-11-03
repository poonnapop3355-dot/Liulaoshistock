from app.crud.base import CRUDBase
from app.schemas.inventory import BookVariant

crud_book_variant = CRUDBase(BookVariant, "/book_variants")
