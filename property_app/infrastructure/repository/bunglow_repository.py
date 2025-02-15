from ...domain.entities.bunglow import Bunglows

from .base_repository import BaseRepository

# sqlalchemy imports
from sqlalchemy.orm import Session

class BunglowRepository(BaseRepository[Bunglows]):
    def __init__(self, db: Session):
        super().__init__(db, Bunglows)
        
        # Bunglow-specific methods can be added here