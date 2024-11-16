from pydantic import BaseModel
from typing import Optional
import uuid

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

    model_config = {"from_attributes": True}