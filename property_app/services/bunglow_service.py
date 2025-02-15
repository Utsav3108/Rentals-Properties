# property imports
from ..domain.models.bunglow_model import BunglowModel
from ..domain.entities.bunglow import Bunglows

# sqlalchemy imports
from sqlalchemy.orm import Session

# service layer imports
from .base_property_service import BasePropertyService

class BunglowService(BasePropertyService):
    def __init__(self, db: Session):
        super().__init__(db, Bunglows, BunglowModel)

# class BunglowService:
    
#     def get_all_bunglows_from_db(self, db : Session, limit : int, offset : int) -> List[BunglowModel]:
        
#         with BaseRepository(db=db) as repo:
#             all_bunglows = repo.get_all_bunglows(limit=limit, offset=offset)
        
#         list_of_bunglows = [ BunglowModel.model_validate(bunglow) for bunglow in all_bunglows ]
        
#         return list_of_bunglows

#     def update_property(self, db : Session, id : uuid.UUID, model: UpdatePropertyModel) -> ResponseModel:
        
#         with BaseRepository(db=db) as repo:
#             prop = repo.update_property(id=id, model=model)

#         if not prop:
#             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Property not found")
        
#         return ResponseModel(status=status.HTTP_200_OK, success=True, data=BunglowModel.model_validate(prop))


#     def get_property(self, db  : Session , id : uuid.UUID):
        
#         with BaseRepository(db=db) as repo:
#             prop = repo.get_property(id=id)
       
#         return BunglowModel.model_validate(prop)

#     def delete_property(self, db : Session, id : uuid.UUID) -> ResponseModel:
        
#         with BaseRepository(db=db) as repo:
#             prop = repo.delete_property(id=id)  
        
        
#         return ResponseModel(data="Property deleted successfully", status=status.HTTP_200_OK, success=True)

#     def count_property(self, db : Session) -> int:
        
#         with BaseRepository(db=db) as repo:
#             count_of_props = repo.count_property()

#         return count_of_props
   
