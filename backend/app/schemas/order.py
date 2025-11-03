from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class Customer(BaseModel):
    id: str
    fullname: str
    phone: Optional[str]
    address_line1: Optional[str]
    subdistrict: Optional[str]
    district: Optional[str]
    province: Optional[str]
    postcode: Optional[str]

class OrderItem(BaseModel):
    book_variant_id: str
    quantity: int
    price: float

class Payment(BaseModel):
    method: str
    amount: float

class Shipment(BaseModel):
    tracking_number: Optional[str]

class Order(BaseModel):
    id: str
    order_no: str
    channel: str
    customer_id: str
    items: List[OrderItem]
    payment: Payment
    shipment: Optional[Shipment]
    created_at: datetime = Field(default_factory=datetime.utcnow)

class InventoryMovement(BaseModel):
    id: str
    variant_id: str
    quantity: int
    type: str  # sale, return, adjustment, transfer
    unit_cost: float
    ref_id: Optional[str]
    created_at: datetime = Field(default_factory=datetime.utcnow)
