from pydantic import BaseModel
from typing import List

class User(BaseModel):
    id: str  # Firebase UID
    email: str
    roles: List[str]  # List of role names
    is_active: bool = True
