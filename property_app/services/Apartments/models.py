from typing import Optional
from pydantic import BaseModel
from property_app.core.model import PropertyModel

class ApartmentModel(PropertyModel):
    bhk : int
    n_floors : int # Number of floors of Apartment
    has_lift : bool
    floor_number : int # floor of the Property
    description : str

    
    # location : Column(Geography(geometry_type='POINT', srid=4326), nullable=True)    

    model_config = {"from_attributes": True}

    def save_property(self, db):
        return super().save_property(db)
    
    

