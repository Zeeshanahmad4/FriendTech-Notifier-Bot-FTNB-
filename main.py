# main.py

from modules.user_input import get_users_of_interest

def main():
    users_of_interest = get_users_of_interest()
    print(f"Monitoring for users: {', '.join(users_of_interest)}")

if __name__ == "__main__":
    main()
