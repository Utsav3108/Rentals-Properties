from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..dependencies import DATABASE_DEPENDENCY
from typing import Type
import uuid
from ...domain.models.standard_models import UpdatePropertyModel

class PropertyRouter:
    def __init__(self, model: Type, schema: Type, service_class: Type, prefix: str):
        self.router = APIRouter(prefix=prefix, tags=[prefix.strip("/")])
        self.model = model
        self.schema = schema
        self.service_class = service_class

        self.router.add_api_route("/", self.get_all_properties, methods=["GET"])
        self.router.add_api_route("/{id}", self.get_property, methods=["GET"])
        self.router.add_api_route("/{id}", self.update_property, methods=["PUT"])
        self.router.add_api_route("/{id}", self.delete_property, methods=["DELETE"])

    def get_all_properties(self, db: Session = DATABASE_DEPENDENCY, limit: int = 10, offset: int = 0):
        service = self.service_class(db)
        return service.get_all_properties(limit=limit, offset=offset)

    def get_property(self, id: uuid.UUID, db: Session = DATABASE_DEPENDENCY):
        service = self.service_class(db)
        return service.get_property(id)

    def update_property(self, id: uuid.UUID, model: UpdatePropertyModel, db: Session = DATABASE_DEPENDENCY):
        service = self.service_class(db)
        return service.update_property(id, model)

    def delete_property(self, id: uuid.UUID, db: Session = DATABASE_DEPENDENCY):
        service = self.service_class(db)
        return service.delete_property(id)
