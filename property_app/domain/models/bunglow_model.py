# fastapi imports
from fastapi import HTTPException, status

# other imports
from typing import List

# property imports
from property_app.domain.models.standard_models import PropertyModel
from property_app.domain.models.standard_models import ResponseModel

# sqlalchemy imports
from sqlalchemy.orm import Session
from sqlalchemy import select

# Bunglows imports
from ..entities.bunglow import Bunglows

# infra imports

class BunglowModel(PropertyModel):
    sqft : str
    no_of_rooms : int
    
    model_config = {"from_attributes" : True}
    
    
    def save_property(self, db : Session) -> ResponseModel:
        super().save_property(db=db)
        
        from  ...infrastructure.repository.bunglow_repository import BunglowRepository
        
        with BunglowRepository(db=db) as repo:
        
            repo.create_property(model=self)
            
        
        success_message = "Bunglow created successfully"
        return ResponseModel(status=status.HTTP_200_OK, success=True, data=success_message)




    