from fittrack.controllers import UserController

def create_user():
    # Create a new user with a unique username
    user = UserController.create_user('test_user', 25, 175, 70, 'intermediate')
    if user:
        print(f"User created: {user}")
    else:
        print("User creation failed.")

if __name__ == "__main__":
    create_user()
