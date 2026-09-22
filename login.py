def login_user(username, password):
    print(f"Logging successful for user: {username} with password: {password}")
    try:
        # Simulate a login process
        if username == "admin" and password == "admin123":
            print("Login successful!")
            return True
        else:
            print("Login failed: Invalid credentials.")
            return False
    except Exception as e:
        print(f"An error occurred during login: {e}")
        return False