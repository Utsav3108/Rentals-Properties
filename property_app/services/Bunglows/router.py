# FastApi imports
from fastapi import APIRouter, HTTPException
from fastapi import status

# property app import
from property_app.services.Bunglows.models import BunglowModel
from property_app.core.dependies import DATABASE_DEPENDENCY
from property_app.core.model import ResponseModel
from property_app.core.exceptions import OPERATIONAL_EXCEPTION, EXCEPTION, TYPE_EXCEPTION

# Sqlalchemy imports
from sqlalchemy.orm import Session
from sqlalchemy.exc import OperationalError, IntegrityError
from property_app.services.Bunglows.schema import Bunglows

# Bunglow imports
from .exceptions import BUNGLOW_INTEGRITY_EXCEPTION

router = APIRouter()


# MARK : Ping API
@router.get("/bunglow_ping")
def bunglowPing():
    return {"message" : "Bunglow is ready to be built."}

# MARK : Create Bunglow
@router.post("/create", response_model=ResponseModel)
def create_bunglow(model : BunglowModel, db : Session = DATABASE_DEPENDENCY):
    
    try : 
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