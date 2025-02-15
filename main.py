# fastapi app for property service
from fastapi import FastAPI

# Database imports
from property_app.core.database import Base, engine

# Router imports
from property_app.api.routers.apartment_router import router as apartment_router
from property_app.api.routers.bunglow_router import router as bunglow_router
from property_app.api.routers.property_router import PropertyRouter

# Domain imports
from property_app.domain.entities.bunglow import Bunglows
from property_app.domain.entities.apartment import Apartment

# Model imports
from property_app.domain.models.apartment_model import ApartmentModel
from property_app.domain.models.bunglow_model import BunglowModel

# Service imports
from property_app.services.bunglow_service import BunglowService
from property_app.services.apartment_service import ApartmentService


app = FastAPI()

# General Routers for Property Types.
app.include_router(PropertyRouter(Bunglows, BunglowModel, BunglowService, "/bunglows").router)
app.include_router(PropertyRouter(Apartment, ApartmentModel, ApartmentService, "/apartments").router)

# Specific Routers for Property Types.
app.include_router(router=apartment_router, prefix="/rentals/apartment", tags=["Apartment"])
app.include_router(router=bunglow_router, prefix="/rentals/bunglow", tags=["Bunglows"])

# Health Check
@app.get("/property_ping", tags=["Health Check"])
def ping():
    return "Property Service is working fine ..."

# Create Tables
@app.on_event("startup")
def start():
    Base.metadata.create_all(bind=engine)
    print("Property Service is starting ...")