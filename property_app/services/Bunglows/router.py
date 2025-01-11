# FastApi imports
from fastapi import APIRouter
from fastapi import status

# property app import
from property_app.services.Bunglows.models import BunglowModel
from property_app.core.dependies import DATABASE_DEPENDENCY
from property_app.core.model import ResponseModel
from property_app.core.exceptions import OPERATIONAL_EXCEPTION, EXCEPTION, TYPE_EXCEPTION

# Sqlalchemy imports
from sqlalchemy.orm import Session
from sqlalchemy.exc import OperationalError, IntegrityError, SQLAlchemyError
from property_app.services.Bunglows.schema import Bunglows
# from sqlalchemy import  select

# general imports
import uuid
from typing import List

# Bunglow imports
from .exceptions import BUNGLOW_INTEGRITY_EXCEPTION
from .controller import get_all_bunglows_from_db

router = APIRouter()


# MARK : Ping API
@router.get("/bunglow_ping")
def bunglowPing():
    return {"message" : "Bunglow is ready to be built."}

# MARK : Create Bunglow
@router.post("/create", response_model=ResponseModel)
def create_bunglow(model : BunglowModel, db : Session = DATABASE_DEPENDENCY):
    
    try : 
        
        model.pid = uuid.uuid4()
        newBunglow = Bunglows(**model.model_dump())
        
        db.add(newBunglow)
        db.commit()
        db.refresh(newBunglow)
        
        success_message = "Bunglow created successfully"
        
        return ResponseModel(status=status.HTTP_200_OK, success=True, data=success_message)
    
    except OperationalError as c:
        raise OPERATIONAL_EXCEPTION
    except IntegrityError as i:
        raise BUNGLOW_INTEGRITY_EXCEPTION
    except TypeError as t:
        raise TYPE_EXCEPTION
    except Exception as e:
        raise EXCEPTION 
    
# MARK : Get Bunglow
@router.get("/allbunglows", response_model=List[BunglowModel])
def get_all_bunglows(limit : int = 10, offset : int = 1, db : Session = DATABASE_DEPENDENCY):
    
    try:
        return get_all_bunglows_from_db(limit=limit, offset=offset, db=db)
    except IntegrityError as i  : 
        print(f"Integrity exception raised: {i}")
        raise BUNGLOW_INTEGRITY_EXCEPTION
    except SQLAlchemyError as s:
        print(f" SQL Alchemy error: {s}")
        raise OPERATIONAL_EXCEPTION
        