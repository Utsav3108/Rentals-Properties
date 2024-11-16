from sqlalchemy import Float
from property_app.core.schema import PropertyBaseModel, Column, String, Integer, Boolean
from geoalchemy2 import Geography


class Apartment(PropertyBaseModel):
    __tablename__ = "Apartments"

    n_floors = Column(Integer, nullable=False)
    floor_number = Column(String(60), nullable=False)
    bhk = Column(Integer, nullable=False)
    has_lift = Column(Boolean, nullable=False)
    description = Column(String(300), nullable=True)

    # New fields
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    location = Column(Geography(geometry_type='POINT', srid=4326), nullable=True)