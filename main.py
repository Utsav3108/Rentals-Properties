from fastapi import FastAPI
from property_app.services.Apartments.router import router as apartment_router

app = FastAPI()
app.include_router(router=apartment_router, prefix="/rentals/property", tags=["Apartment"])

@app.get("/property_ping", tags=["Health Check"])
def ping():
    return "Property Service is working fine ..."
