from pydantic import BaseModel
from typing import List, Optional

class BookVariant(BaseModel):
    id: str
    sku: str
    scan_code: Optional[str]
    price: float
    cost: float
    tax_rate: float
    min_stock: int
    shelf_bin: Optional[str]
    active: bool = True
    book_id: str

class Category(BaseModel):
    id: str
    name: str

class Supplier(BaseModel):
    id: str
    name: str
    credit_terms: Optional[str]

class PurchaseOrderItem(BaseModel):
    book_variant_id: str
    quantity: int
    unit_cost: float

class PurchaseOrder(BaseModel):
    id: str
    supplier_id: str
    items: List[PurchaseOrderItem]
