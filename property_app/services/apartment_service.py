# base property service imports
from .base_property_service import BasePropertyService

# property imports
from ..domain.entities.apartment import Apartment
from ..domain.models.apartment_model import ApartmentModel

# sqlalchemy imports
from sqlalchemy.orm import Session

class ApartmentService(BasePropertyService):
    def __init__(self, db: Session):
        super().__init__(db, Apartment, ApartmentModel)








# from fastapi import HTTPException
# from sqlalchemy.orm import Session
# from ..domain.entities.apartment import Apartment
# from ..domain.models.apartment_model import ApartmentModel
# from property_app.domain.models.standard_models import UpdatePropertyModel
# from sqlalchemy.future import select
# from fastapi import status
# import uuid


# # ================ Exception ============================
# PROPERTY_NOT_FOUND = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Property not found")

# from sqlalchemy import func

# # =============== Methods ============================
# def create_apartment(db = Session, apartment = Apartment):
#     db_aptmt = apartment
#     db.add(db_aptmt)
#     db.commit()
#     db.refresh(db_aptmt)
#     return db_aptmt

# def map(aptm = ApartmentModel) -> Apartment :
#     apt = Apartment(
#         pid = uuid.uuid4(),
#         landlord_id = aptm.landlord_id,
#         landlord_email = aptm.landlord_email,
#         property_name = aptm.property_name,
#         property_rent = aptm.property_rent,
#         property_blocknumber = aptm.property_blocknumber, # A7, C68 etc
#         property_societyname = aptm.property_societyname,
#         property_landmark = aptm.property_landmark,
#         property_city = aptm.property_city,
#         property_pincode = aptm.property_pincode,
#         property_state = aptm.property_state,
#         property_district = aptm.property_district,
#         property_country = aptm.property_country,
#         property_available = aptm.property_available,
#         bhk = aptm.bhk,
#         n_floors = aptm.bhk,
#         has_lift = aptm.has_lift,
#         floor_number = aptm.floor_number, # floor of the Property
#         description = aptm.description,
#         latitude = aptm.latitude,
#         longitude = aptm.longitude
#     )

#     return apt


# def get_available_property(db: Session, limit: int, offset: int):
#     # Fetch properties with pagination using limit and offset
#     result = db.execute(
#         select(Apartment)
#         .where(Apartment.property_available == True)  # Assuming we fetch only available properties
#         .limit(limit)
#         .offset(offset)
#     )
#     properties = result.scalars().all()
    
#     if not properties:
#         raise PROPERTY_NOT_FOUND

#     # Convert each SQLAlchemy object to a Pydantic model
#     return [ApartmentModel.model_validate(prop) for prop in properties]


# # Function to fetch all apartments with pagination support
# def get_all_apartments(db: Session, limit: int, offset: int):
#     # Fetch all apartments with pagination using limit and offset
#     result = db.execute(
#         select(Apartment)
#         .limit(limit)
#         .offset(offset)
#     )
#     apartments = result.scalars().all()
    
#     if not apartments:
#         raise PROPERTY_NOT_FOUND

#     # Convert SQLAlchemy objects to Pydantic models
#     return [ApartmentModel.model_validate(apartment) for apartment in apartments]


# # Function to update property in the database
# def update_property(db: Session, pid: uuid.UUID, property_data: UpdatePropertyModel):
#     # Fetch the property by its ID
#     property_obj = db.execute(select(Apartment).where(Apartment.pid == pid)).scalars().first()
    
#     if not property_obj:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Property not found")
    
#     # Update each field if provided
#     for field, value in property_data.dict(exclude_unset=True).items():
#         setattr(property_obj, field, value)
    
#     db.commit()  # Commit the transaction to save changes
#     db.refresh(property_obj)  # Refresh to get updated property data
    
#     return property_obj