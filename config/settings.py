# config/settings.py

# API configurations
BASE_URL = "https://api.friend.tech"  # Placeholder URL
API_KEY = "YOUR_API_KEY_HERE"

# Common API endpoints (assuming some common endpoints, you can adjust as needed)
USER_ENDPOINT = f"{BASE_URL}/users"
CHAT_ENDPOINT = f"{BASE_URL}/chat"
VOTING_ENDPOINT = f"{BASE_URL}/voting"

# Standard headers for API requests
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Other configurations can be added as the project progresses

def handle_api_response(response):
    """
    Handles the API response. 
    Parses the JSON and returns the data or raises an exception for non-2xx responses.

    Args:
    - response: The API response object.

    Returns:
    - Parsed JSON data from the response.
    """
    if 200 <= response.status_code < 300:
        return response.json()
    else:
        response.raise_for_status()

def log_error(error):
    """
    Logs the error for debugging purposes. 
    This can be enhanced to log to a file or an external service.

    Args:
    - error: The error message or exception to log.
    """
    print(f"Error encountered: {error}")

