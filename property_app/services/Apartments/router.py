from typing import List
import uuid
from fastapi import Query
from fastapi.routing import APIRouter


from .models import ApartmentModel
from property_app.core.model import UpdatePropertyModel
from sqlalchemy.orm import Session
from sqlalchemy import func
from .schema import Apartment
from property_app.core.dependies import DATABASE_DEPENDENCY

from .controller import get_available_property, get_all_apartments, update_property

router = APIRouter()

@router.post("/listing/apartment")
def create_property(apartment : ApartmentModel, db : Session = DATABASE_DEPENDENCY):
    from .controller import create_apartment, map

    apt = map(aptm=apartment)
    apt.location=f'SRID=4326;POINT({apt.latitude} {apt.longitude})'
    create_apartment(db = db, apartment = apt)
    return {"message": "Property Created"}


# /apartment/available?limit=10&offset=0

@router.get("/apartment/available", response_model=List[ApartmentModel])
def select_property_available(
    db: Session = DATABASE_DEPENDENCY,
    limit: int = Query(10, ge=1),  # Number of properties per page
    offset: int = Query(0, ge=0)   # Start position in the database
):

    prop = get_available_property(db=db, limit=limit, offset=offset)
    return prop

@router.get("/apartments", response_model=List[ApartmentModel])
def list_all_apartments(
    db: Session = DATABASE_DEPENDENCY,
    limit: int = Query(10, ge=1),  # Number of properties per page
    offset: int = Query(0, ge=0)   # Start position in the database
):
    apartments = get_all_apartments(db=db, limit=limit, offset=offset)
    return apartments

# Define the endpoint to update a property
@router.patch("/apartments/{pid}", response_model=ApartmentModel)
def update_apartment(
    pid: uuid.UUID,
    property_data: UpdatePropertyModel,
    db: Session = DATABASE_DEPENDENCY
):
    updated_property = update_property(db=db, pid=pid, property_data=property_data)
    return ApartmentModel.model_validate(updated_property)


# ================================= Near by Location ========================================
@router.get("/nearby_apartments", response_model=List[ApartmentModel])
def get_nearby_apartments(latitude: float, longitude: float, radius: float, db: Session = DATABASE_DEPENDENCY):
    radius_meters = radius * 1000  # Convert radius to meters
    nearby_apartments = db.query(Apartment).filter(
        func.ST_DWithin(
            Apartment.location,
            func.ST_SetSRID(func.ST_MakePoint(longitude, latitude), 4326),
            radius_meters
        )
    ).all()
    return nearby_apartments