from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.crud.user import crud_user
from app.schemas.user import User
from app.core.auth import get_current_user
from app.core.rbac import require_role

router = APIRouter()

@router.post("/", response_model=User, dependencies=[Depends(require_role(["admin"]))])
def create_user(user: User):
    return crud_user.create(user)

@router.get("/", response_model=List[User], dependencies=[Depends(require_role(["admin", "manager"]))])
def read_users():
    return crud_user.get_multi()

@router.get("/me", response_model=User)
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
