import time
while True:
    password = input("Enter your password: ")
    time.sleep(2)
    print("Please wait while we verify your password...")
    time.sleep(2)
    if len(password) < 8:
        print("Password is too short. Please use at least 8 characters.")
    elif not any(char.isdigit() for char in password):
        print("Password must contain at least one number.")
    elif not any(char.isupper() for char in password):
        print("Password must contain at least one uppercase letter.")
    elif not any(char.islower() for char in password):
        print("Password must contain at least one lowercase letter.")
    else:
        print("Password is valid!")

    again = input("Would you like to try again? (yes/no): ").strip().lower()
    if again not in ("yes", "y"):
        print("Goodbye!")
        break