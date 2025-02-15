import requests

from fastapi import HTTPException


from ..core.config import AUTH_BASE_URL, AUTH_TOKEN
class UserService:
    def get_user_details():
        
        URL = AUTH_BASE_URL + "rentals/user"

        # Set the headers to include the authorization token
        headers = {
            "Authorization": f"Bearer {AUTH_TOKEN}"
        }

        try:
            # Make the GET request to the user service
            response = requests.get(URL, headers=headers)
            response.raise_for_status()  # Raise an exception for non-2xx status codes
        except requests.exceptions.RequestException as e:
            raise HTTPException(status_code=500, detail=f"Failed to fetch user details: {str(e)}")
        
        print("User Details Response : ", response.json())
        # Parse the JSON response and return it
        return True