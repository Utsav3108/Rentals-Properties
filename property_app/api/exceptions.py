from sqlalchemy.exc import OperationalError, IntegrityError
from fastapi import HTTPException
from fastapi import status

OPERATIONAL_EXCEPTION = HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                      detail="Failed to connect to the database. Please try again later.")


TYPE_EXCEPTION = HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Data serialization error occurred. Please contact support."
        )

EXCEPTION = HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred. Please try again later."
        )