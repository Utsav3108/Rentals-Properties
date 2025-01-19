# fastapi imports
from fastapi import HTTPException, status

# property imports
from property_app.core.dependies import DATABASE_DEPENDENCY
from property_app.core.model import UpdatePropertyModel, ResponseModel
from property_app.services.Bunglows.models import BunglowModel
from property_app.core.config import AUTH_BASE_URL, AUTH_TOKEN

# sqlalchemy imports
from sqlalchemy.orm import Session
from sqlalchemy import select

# bunglow imports
from .schema import Bunglows

# general imports
from typing import List
import uuid
import requests

# MARK: Get all bunglows controller
def get_all_bunglows_from_db(limit : int, offset : int, db : Session = DATABASE_DEPENDENCY) -> List[BunglowModel]:
    
    all_bunglows = db.execute(select(Bunglows)
                              .limit(limit=limit)
                              .offset(offset=offset)
                              ).scalars().all()
    
    list_of_bunglows = [ BunglowModel.model_validate(bunglow) for bunglow in all_bunglows ]
    
    return list_of_bunglows

def update_property(db : Session, id : uuid.UUID, model: UpdatePropertyModel) -> ResponseModel:
    
    prop = _get_property(db=db, id=id)
    
    if not prop:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Property not found")
    
    for field, value in model.dict(exclude_unset=True).items():
        setattr(prop, field, value)
    
    db.commit()
    db.refresh(prop)
    
    return ResponseModel(status=status.HTTP_200_OK, success=True, data=BunglowModel.model_validate(prop))


def _get_property(db  : Session , id : uuid.UUID):
    
    prop = db.execute(select(Bunglows).where(Bunglows.pid == id)).scalars().first()
    
    return prop

def delete_property(db : Session, id : uuid.UUID) -> ResponseModel:
    prop = _get_property(db=db, id=id)
    
    if not prop: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Property not found")
    
    db.delete(prop)
    db.commit()
    
    
    return ResponseModel(data="Proerty deleted successfully", status=status.HTTP_200_OK, success=True)

def count_property(db : Session) -> int:
    all_bunglows = db.execute(select(Bunglows)).scalars().all()
    
    count_of_props = len(all_bunglows)
    
    return count_of_props
   
def get_user_details():
    
    URL = AUTH_BASE_URL + "rentals/user"

    # Set the headers to include the authorization token
    headers = {
        "Authorization": f"Bearer {AUTH_TOKEN}"
    }

    try:
        # Make the GET request to the user service
        response = requests.get(URL, headers=headers)
        response.raise_for_status()  # Raise an exception for non-2xx status codes
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch user details: {str(e)}")
    
    print("User Details Response : ", response.json())
    # Parse the JSON response and return it
    return True