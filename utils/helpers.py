# utils/helpers.py

from datetime import datetime

def validate_data(data):
    """
    Validates if the given data is not None or an empty string.

    Args:
    - data: Data to validate.

    Returns:
    - True if data is valid, False otherwise.
    """
    if data is None or (isinstance(data, str) and not data.strip()):
        return False
    return True

def format_date(date_obj, format_str="%Y-%m-%d %H:%M:%S"):
    """
    Formats a datetime object into a readable string format.

    Args:
    - date_obj (datetime.datetime): Datetime object to format.
    - format_str (str, optional): Desired format. Defaults to "%Y-%m-%d %H:%M:%S".

    Returns:
    - Formatted date string.
    """
    return date_obj.strftime(format_str)

def get_from_dict(data_dict, key, default=None):
    """
    Safely retrieves a value from a dictionary. 
    Returns a default value if the key doesn't exist.

    Args:
    - data_dict (dict): Dictionary to fetch data from.
    - key: Key to retrieve the value for.
    - default: Default value to return if key is not found.

    Returns:
    - Value associated with the key or default.
    """
    return data_dict.get(key, default)

def log_message(message):
    """
    Logs a message. This is a placeholder and can be enhanced 
    to log to files or external systems.

    Args:
    - message (str): Message to log.
    """
    print(f"[{format_date(datetime.now())}] {message}")

