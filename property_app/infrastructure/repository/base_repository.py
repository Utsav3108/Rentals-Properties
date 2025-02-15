# sqlalchemy imports
from sqlalchemy import select
from sqlalchemy.orm import Session
from typing import Type, TypeVar, Generic

# Define a generic type variable
T = TypeVar("T")

class BaseRepository(Generic[T]):
    def __init__(self, db: Session, model: Type[T]):
        self.db = db
        self.model = model

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.db.close()

    def get_all(self, offset: int, limit: int):
        return self.db.execute(
            select(self.model).limit(limit).offset(offset)
        ).scalars().all()

    def get_by_id(self, id):
        return self.db.execute(
            select(self.model).where(self.model.pid == id)
        ).scalars().first()

    def update(self, id, model):
        prop = self.get_by_id(id)
        if not prop:
            return None
        
        for field, value in model.dict(exclude_unset=True).items():
            setattr(prop, field, value)

        self.db.commit()
        self.db.refresh(prop)
        return prop

    def delete(self, id):
        prop = self.get_by_id(id)
        if not prop:
            return None
        
        self.db.delete(prop)
        self.db.commit()
        return prop

    def count(self):
        return len(self.db.execute(select(self.model)).scalars())

    def create(self, model):
        prop = self.model(**model.dict())
        self.db.add(prop)
        self.db.commit()
        self.db.refresh(prop)
        return prop
