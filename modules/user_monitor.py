# modules/user_monitor.py

from modules.notification import send_notification

def check_new_user(username, users_of_interest):
    """
    Checks if a new user is in the list of users of interest.
    If yes, sends a notification.
    """
    if username in users_of_interest:
        send_notification(username)
