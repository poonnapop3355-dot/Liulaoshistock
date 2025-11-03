from app.crud.base import CRUDBase
from app.schemas.user import User

crud_user = CRUDBase(User, "/users")
