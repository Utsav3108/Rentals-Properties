from fastapi import status

from typing import List
import uuid

from property_app.core.dependies import DATABASE_DEPENDENCY
from property_app.core.model import PropertyModel
from property_app.core.model import ResponseModel

from sqlalchemy.orm import Session
from sqlalchemy import select

from .schema import Bunglows

class BunglowModel(PropertyModel):
    sqft : str
    no_of_rooms : int
    
    model_config = {"from_attributes" : True}
    
    
    def save_property(self, db : Session) -> ResponseModel:
        super().save_property(db=db)
        
        newBunglow = Bunglows(**self.model_dump())
        
        db.add(newBunglow)
        db.commit()
        db.refresh(newBunglow)
        
        success_message = "Bunglow created successfully"
        return ResponseModel(status=status.HTTP_200_OK, success=True, data=success_message)


    
    