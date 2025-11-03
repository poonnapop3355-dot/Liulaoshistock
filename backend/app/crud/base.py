from typing import Any, Dict, Generic, List, Optional, Type, TypeVar
from pydantic import BaseModel
from app.db.firebase import get_db

ModelType = TypeVar("ModelType", bound=BaseModel)

class CRUDBase(Generic[ModelType]):
    def __init__(self, model: Type[ModelType], db_path: str):
        self.model = model
        self.db_path = db_path
        self.db = get_db()

    def get(self, id: str) -> Optional[ModelType]:
        data = self.db.reference(f"{self.db_path}/{id}").get()
        if data:
            return self.model(**data)
        return None

    def get_multi(self) -> List[ModelType]:
        data = self.db.reference(self.db_path).get()
        if data:
            return [self.model(**item) for item in data.values()]
        return []

    def create(self, obj_in: ModelType) -> ModelType:
        self.db.reference(f"{self.db_path}/{obj_in.id}").set(obj_in.dict())
        return obj_in

    def update(self, id: str, obj_in: Dict[str, Any]) -> Optional[ModelType]:
        self.db.reference(f"{self.db_path}/{id}").update(obj_in)
        return self.get(id)

    def remove(self, id: str) -> None:
        self.db.reference(f"{self.db_path}/{id}").delete()
