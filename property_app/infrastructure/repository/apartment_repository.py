from ...domain.entities.apartment import Apartment

from .base_repository import BaseRepository

# sqlalchemy imports
from sqlalchemy.orm import Session

class ApartmentRepository(BaseRepository[Apartment]):
    def __init__(self, db: Session):
        super().__init__(db, Apartment)
        
        # Bunglow-specific methods can be added here