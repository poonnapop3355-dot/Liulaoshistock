from app.crud.base import CRUDBase
from app.schemas.inventory import BookVariant, Category, Supplier, PurchaseOrder

crud_book_variant = CRUDBase(BookVariant, "/book_variants")
crud_category = CRUDBase(Category, "/categories")
crud_supplier = CRUDBase(Supplier, "/suppliers")
crud_purchase_order = CRUDBase(PurchaseOrder, "/purchase_orders")
