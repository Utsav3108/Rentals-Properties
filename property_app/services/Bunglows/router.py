# FastApi imports
from fastapi import APIRouter, HTTPException, status

# property app import
from property_app.services.Bunglows.models import BunglowModel
from property_app.core.dependies import DATABASE_DEPENDENCY
from property_app.core.model import ResponseModel, UpdatePropertyModel
from property_app.core.exceptions import OPERATIONAL_EXCEPTION, EXCEPTION, TYPE_EXCEPTION

# Sqlalchemy imports
from sqlalchemy.orm import Session
from sqlalchemy.exc import OperationalError, IntegrityError, SQLAlchemyError
from property_app.services.Bunglows.schema import Bunglows

# general imports
from typing import List
import uuid

# Bunglow imports
from .exceptions import BUNGLOW_INTEGRITY_EXCEPTION
from .controller import get_all_bunglows_from_db, get_property, update_property
router = APIRouter()


# MARK : Ping API
@router.get("/bunglow_ping")
def bunglowPing():
    return {"message" : "Bunglow is ready to be built."}

# MARK : Create Bunglow
@router.post("/create", response_model=ResponseModel)
def create_bunglow(model : BunglowModel, db : Session = DATABASE_DEPENDENCY):
    
    try : 
        return model.save_property(db = db)
    except OperationalError as c:
        raise OPERATIONAL_EXCEPTION
    except IntegrityError as i:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail=f"{i}")
    except TypeError as t:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"{t}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"{e}"
        ) 
    
# MARK : Get Bunglow
@router.get("/allbunglows")
def get_all_bunglows(limit : int = 10, offset : int = 1, db : Session = DATABASE_DEPENDENCY):
    
    try:
        
        all_bunglows = get_all_bunglows_from_db(db=db,limit=limit,offset=offset)
        
        return all_bunglows
    except IntegrityError as i  : 
        print(f"Integrity exception raised: {i}")
        raise BUNGLOW_INTEGRITY_EXCEPTION
    except SQLAlchemyError as s:
        print(f" SQL Alchemy error: {s}")
        raise OPERATIONAL_EXCEPTION
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"{e}"
        ) 
        
@router.patch("/update", response_model=ResponseModel)
def update_bunglow(id : uuid.UUID, update_fields : UpdatePropertyModel, db : Session = DATABASE_DEPENDENCY):
    
    return update_property(db=db,id=id, model=update_fields)
    
@router.get("/get_property")
def get_bunglow_by_id(id: uuid.UUID, db: Session = DATABASE_DEPENDENCY):
    return BunglowModel.model_validate(get_property(db=db, id=id))