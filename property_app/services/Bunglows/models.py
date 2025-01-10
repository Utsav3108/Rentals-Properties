from property_app.core.model import PropertyModel

class BunglowModel(PropertyModel):
    sqft : str
    no_of_rooms : int
    
    model_config = {"from_attributes" : True}