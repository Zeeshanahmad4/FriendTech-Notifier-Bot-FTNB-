# modules/user_input.py

def get_users_of_interest():
    """
    Collects a list of usernames of interest from the user.
    """
    users = []
    print("Enter usernames of interest (type 'done' when finished):")
    while True:
        username = input()
        if username.lower() == 'done':
            break
        users.append(username)
    return users
 
