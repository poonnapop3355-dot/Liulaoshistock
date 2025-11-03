from fastapi import Depends, HTTPException
from app.core.auth import get_current_user
from app.schemas.user import User
from typing import List

def require_role(required_roles: List[str]):
    def role_checker(current_user: User = Depends(get_current_user)):
        if not any(role in current_user.roles for role in required_roles):
            raise HTTPException(status_code=403, detail="Not authorized")
        return current_user
    return role_checker
