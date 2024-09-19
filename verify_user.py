from fittrack.controllers import UserController

def check_user(username):
    user = UserController.get_user(username)
    if user:
        print(f"User found: {user}")
    else:
        print("User not found.")

if __name__ == "__main__":
    check_user('test_user')  # Replace 'test_user' with the username you're using
