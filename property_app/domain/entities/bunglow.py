from property_app.domain.entities.property_base import PropertyBaseModel, Column, String, Integer


class Bunglows(PropertyBaseModel):
    __tablename__ = "Bunglows"
    
    sqft = Column(String, nullable=False )
    no_of_rooms = Column(Integer, nullable=False)
    
    
    