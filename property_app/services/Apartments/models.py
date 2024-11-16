from typing import Optional
from pydantic import BaseModel
from property_app.core.model import PropertyModel

class ApartmentModel(PropertyModel):
    bhk : int
    n_floors : int # Number of floors of Apartment
    has_lift : bool
    floor_number : int # floor of the Property
    description : str

    latitude : float
    longitude : float
    # location : Column(Geography(geometry_type='POINT', srid=4326), nullable=True)    

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


