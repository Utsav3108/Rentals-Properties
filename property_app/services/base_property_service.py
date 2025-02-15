from sqlalchemy.orm import Session
from ..infrastructure.repository.base_repository import BaseRepository
from ..domain.models.standard_models import ResponseModel, UpdatePropertyModel
from fastapi import HTTPException, status
from typing import Type, TypeVar, List
import uuid

T = TypeVar("T")  # Generic Type for different property models
M = TypeVar("M")  # Generic Type for different Pydantic models

class BasePropertyService:
    def __init__(self, db: Session, model: Type[T], schema: Type[M]):
        self.db = db
        self.model = model  # Database Model (e.g., Bunglows, Apartment)
        self.schema = schema  # Pydantic Model (e.g., BunglowModel, ApartmentModel)

    def get_all_properties(self, limit: int, offset: int) -> List[M]:
        with BaseRepository(db=self.db, model=self.model) as repo:
            properties = repo.get_all(offset=offset, limit=limit)
        return [self.schema.model_validate(prop) for prop in properties]

    def get_property(self, id: uuid.UUID) -> M:
        with BaseRepository(db=self.db, model=self.model) as repo:
            prop = repo.get_by_id(id=id)
        if not prop:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Property not found")
        return self.schema.model_validate(prop)

    def update_property(self, id: uuid.UUID, model: UpdatePropertyModel) -> ResponseModel:
        with BaseRepository(db=self.db, model=self.model) as repo:
            prop = repo.update(id=id, model=model)
        if not prop:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Property not found")
        return ResponseModel(status=status.HTTP_200_OK, success=True, data=self.schema.model_validate(prop))

    def delete_property(self, id: uuid.UUID) -> ResponseModel:
        with BaseRepository(db=self.db, model=self.model) as repo:
            prop = repo.delete(id=id)
        if not prop:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Property not found")
        return ResponseModel(data="Property deleted successfully", status=status.HTTP_200_OK, success=True)

    def count_properties(self) -> int:
        with BaseRepository(db=self.db, model=self.model) as repo:
            count = repo.count()
        return count
