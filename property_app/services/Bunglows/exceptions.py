from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status

BUNGLOW_INTEGRITY_EXCEPTION = HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                            detail="A bungalow with this data already exists or violates integrity constraints.")

