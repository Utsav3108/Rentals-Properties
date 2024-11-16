from .database import get_db
from fastapi import Depends

DATABASE_DEPENDENCY = Depends(get_db)