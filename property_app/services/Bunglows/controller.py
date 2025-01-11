# property imports
from property_app.core.dependies import DATABASE_DEPENDENCY
from property_app.services.Bunglows.models import BunglowModel

# sqlalchemy imports
from sqlalchemy.orm import Session
from sqlalchemy import select

# bunglow imports
from .schema import Bunglows

# general imports
from typing import List


# MARK: Get all bunglows controller
def get_all_bunglows_from_db(limit : int, offset : int, db : Session = DATABASE_DEPENDENCY) -> List[BunglowModel]:
    
    all_bunglows = db.execute(select(Bunglows)
                              .limit(limit=limit)
                              .offset(offset=offset)
                              ).scalars().all()
    
    list_of_bunglows = [ BunglowModel.model_validate(bunglow) for bunglow in all_bunglows ]
    
    return list_of_bunglows