# FastApi imports
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

# property app import
from property_app.core.config  import TOKEN_URL
from property_app.services.Bunglows.models import BunglowModel
from property_app.core.dependies import DATABASE_DEPENDENCY
from property_app.core.model import ResponseModel, UpdatePropertyModel
from property_app.core.exceptions import OPERATIONAL_EXCEPTION
# Sqlalchemy imports
from sqlalchemy.orm import Session
from sqlalchemy.exc import OperationalError, IntegrityError, SQLAlchemyError

# general imports
import uuid

# Bunglow imports
from .exceptions import BUNGLOW_INTEGRITY_EXCEPTION
from .controller import get_user_details

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl=TOKEN_URL)

# MARK : Ping API
@router.get("/bunglow_ping")
def bunglowPing():
    get_user_details()
    return {"message" : "Bunglow is ready to be built."}

@router.get("/count")
def count_of_bunglows(db : Session = DATABASE_DEPENDENCY, token : OAuth2PasswordBearer = Depends(oauth2_scheme)):
    
    from .controller import count_property
    
    return count_property(db=db)

@router.get("/get_property")
def get_bunglow_by_id(id: uuid.UUID, db: Session = DATABASE_DEPENDENCY):
    
    from .controller import _get_property

    return BunglowModel.model_validate(_get_property(db=db, id=id))

# MARK : Get Bunglow
@router.get("/allbunglows")
def get_all_bunglows(limit : int = 10, offset : int = 1, db : Session = DATABASE_DEPENDENCY):
    from .controller import get_all_bunglows_from_db

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
          
@router.patch("/update", response_model=ResponseModel)
def update_bunglow(id : uuid.UUID, update_fields : UpdatePropertyModel, db : Session = DATABASE_DEPENDENCY):
    
    from .controller import update_property

    return update_property(db=db,id=id, model=update_fields)
    

@router.delete("/delete")
def delete_bunglow(id : uuid.UUID, db : Session = DATABASE_DEPENDENCY):
    from .controller import delete_property
    return delete_property(db=db, id=id)


