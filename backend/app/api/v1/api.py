from fastapi import APIRouter
from app.api.v1.endpoints import books, users, pos, orders, shipping, catalog, book_variants

api_router = APIRouter()
api_router.include_router(books.router, prefix="/books", tags=["books"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(pos.router, prefix="/pos", tags=["pos"])
api_router.include_router(orders.router, prefix="/orders", tags=["orders"])
api_router.include_router(shipping.router, prefix="/shipping", tags=["shipping"])
api_router.include_router(catalog.router, prefix="/catalog", tags=["catalog"])
api_router.include_router(book_variants.router, prefix="/book_variants", tags=["book_variants"])
