

class Authentcation(object):
    def __init__(self, username=None, password=None):
        # Initialize the class with optional username and password
        # If username and password are provided, set them
        # Otherwise, set them to None
        self.username = username
        self.password = password
        # Initialize an empty dictionary to store users
        # The keys will be usernames and the values will be passwords
        self.users = {}
    def __str__(self):
        # Return a string representation of the class
        # If username and password are not None, return them
        return f"Username: {self.username}, Password: {self.password}"


    def createAccount(self):
        # Prompt the user to enter a username and password
        self.username = input("Enter username: ")
        self.password = input("Enter password: ")
        #save the username and password in the users dictionary
        self.users[self.username] = self.password
        print("Account created successfully")
        return True
    def Login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        # Check if the username exists in the users dictionary
        if username in self.users and self.users[username] == password:
            print("Login successful")
            return True
        else:
            print("Invalid username or password")
            raise ValueError("Invalid username or password")


def main():
    auth = Authentcation()
    while True:
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        try:
            if choice == '1':
                auth.createAccount()
            elif choice == '2':
                auth.Login()
            elif choice == '3':
                break
            else:
                print("Invalid choice, please try again.")
        except ValueError as e:
            print(e)
if __name__ == "__main__":
    main()