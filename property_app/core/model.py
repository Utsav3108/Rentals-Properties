from pydantic import BaseModel
from typing import Optional
import uuid
from fastapi import status



class PropertyModel(BaseModel):
    pid : uuid.UUID = uuid.uuid4()
    landlord_id : uuid.UUID
    landlord_email : str
    property_name : Optional[str]
    property_rent : int
    property_blocknumber : str # A7, C68 etc
    property_societyname : str
    property_landmark : str
    property_city : str
    property_pincode : int
    property_state : str
    property_district : str
    property_country : str
    property_available : bool
    
    latitude : float
    longitude : float

    model_config = {"from_attributes": True}
    
# Define a Pydantic model for updating a property
class UpdatePropertyModel(BaseModel):
    property_name: Optional[str] = None
    property_blocknumber: Optional[str] = None
    property_societyname: Optional[str] = None
    property_landmark: Optional[str] = None
    property_city: Optional[str] = None
    property_pincode: Optional[int] = None
    property_state: Optional[str] = None
    property_district: Optional[str] = None
    property_country: Optional[str] = None
    property_available: Optional[bool] = None

    model_config = {"from_attributes": True}  # Enables ORM support

class ResponseModel(BaseModel):
    success : bool
    status : int
    data : Optional[any] = None
    
    class Config:
        arbitrary_types_allowed = True
    