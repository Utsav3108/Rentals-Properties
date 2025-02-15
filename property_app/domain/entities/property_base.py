from sqlalchemy import Column, Integer, String, Boolean, Float
from property_app.core.database import Base
from sqlalchemy.dialects.postgresql import UUID
from geoalchemy2 import Geography
import uuid


class PropertyBaseModel(Base):

    __abstract__ = True

    pid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    landlord_id = Column(UUID(as_uuid=True), nullable=False)
    landlord_email = Column(String(60), nullable=False)
    property_name = Column(String(60), nullable=True)
    property_rent = Column(Integer, nullable=False)
    property_blocknumber = Column(String(10), nullable=False)
    property_societyname = Column(String(100), nullable=False)
    property_landmark = Column(String(100), nullable=False)
    property_city = Column(String(100), nullable=False)
    property_pincode = Column(Integer, nullable=False)
    property_state = Column(String(60), nullable=False)
    property_district = Column(String(100), nullable=False)
    property_country = Column(String(60), nullable=False)
    property_available = Column(Boolean, nullable=False)

    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    location = Column(Geography(geometry_type='POINT', srid=4326), nullable=True)

    