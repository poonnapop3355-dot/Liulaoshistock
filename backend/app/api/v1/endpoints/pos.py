from fastapi import APIRouter, Depends, HTTPException
from app.schemas.order import Order, InventoryMovement
from app.crud.order import crud_order, crud_inventory_movement
from app.core.rbac import require_role
import uuid
from datetime import datetime

router = APIRouter()

@router.post("/orders", response_model=Order, dependencies=[Depends(require_role(["admin", "manager", "staff-pos"]))])
def create_pos_order(order: Order):
    """
    Create a new Point of Sale order.
    This will also create corresponding inventory movements to deduct stock.
    """
    # 1. Save the order
    order.id = str(uuid.uuid4())
    order.created_at = datetime.utcnow()
    created_order = crud_order.create(order)

    # 2. Create inventory movements for each item in the order
    for item in order.items:
        movement = InventoryMovement(
            id=str(uuid.uuid4()),
            variant_id=item.book_variant_id,
            quantity=-item.quantity,  # Deduct stock
            type="sale",
            unit_cost=0, # In a real scenario, this would be fetched from the variant
            ref_id=created_order.id,
            created_at=datetime.utcnow()
        )
        crud_inventory_movement.create(movement)

    return created_order
