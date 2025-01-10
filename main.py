from fastapi import FastAPI
from property_app.services.Apartments.router import router as apartment_router
from property_app.services.Bunglows.router import router as bunglow_router

app = FastAPI()
app.include_router(router=apartment_router, prefix="/rentals/apartment", tags=["Apartment"])
app.include_router(router=bunglow_router, prefix="/rentals/bunglow", tags=["Bunglows"])

@app.get("/property_ping", tags=["Health Check"])
def ping():
    return "Property Service is working fine ..."
