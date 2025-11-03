from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.schemas.order import Order
from app.crud.order import crud_order
from app.core.rbac import require_role

router = APIRouter()

@router.get("/", response_model=List[Order], dependencies=[Depends(require_role(["admin", "manager", "packer"]))])
def read_orders():
    """
    Retrieve all orders.
    """
    return crud_order.get_multi()

@router.get("/{order_id}", response_model=Order, dependencies=[Depends(require_role(["admin", "manager", "packer"]))])
def read_order(order_id: str):
    """
    Retrieve a specific order by ID.
    """
    db_order = crud_order.get(order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order

@router.put("/{order_id}/status", response_model=Order, dependencies=[Depends(require_role(["admin", "manager"]))])
def update_order_status(order_id: str, status: str):
    """
    Update the status of an order.
    """
    db_order = crud_order.get(order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")

    # In a real application, you would have more complex status transition logic
    updated_order = crud_order.update(order_id, {"status": status})
    return updated_order
