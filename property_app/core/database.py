from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .config import DB_NAME, DB_PASSWORD, DB_USER, DB_HOST, DB_PORT
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

print("database url: ", DATABASE_URL)
engine = create_engine(DATABASE_URL)


SessionLocal = sessionmaker(autocommit = False, bind = engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()
