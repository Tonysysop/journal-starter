# api/security.py

import os
from fastapi import Security, HTTPException, status
from fastapi.security import APIKeyHeader

# This is where we'll expect the API Key to be in the request header.
# For example: X-API-Key: your_secret_api_key
api_key_header = APIKeyHeader(name="X-API-Key")

# This is your secret API key. In a real application, you should load this
# from an environment variable or a secrets management service.
# For this example, we'll hardcode it.
API_KEY = os.environ.get("API_KEY", "Accesskey") 

def get_api_key(api_key: str = Security(api_key_header)):
    """
    Takes the API key from the header and validates it.
    
    This function is a dependency that can be used in your endpoints.
    """
    if api_key == API_KEY:
        return api_key
    else:
        # If the key is invalid, we raise an exception.
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API Key",
        )