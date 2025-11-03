from app.crud.base import CRUDBase
from app.schemas.order import Customer, Order, InventoryMovement

crud_customer = CRUDBase(Customer, "/customers")
crud_order = CRUDBase(Order, "/orders")
crud_inventory_movement = CRUDBase(InventoryMovement, "/inventory_movements")
