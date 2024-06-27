"""
file = open("storage.txt", "r")
var = file.read()
print(var)

"""

"""
line = (line.strip() for line in open ("storage.txt"))
for line in line:
    print(line)

"""

"""
file = open("storage.txt", "w")
[print("HELLO")]
[print("PANDEJO")]
file.close()
"""

import random

class Store:
    def __init__(self):
        self.users = self.load_users()
        print("W3lC0M3 \n")

    def load_users(self):
        try:
            with open("accounts.txt", "r") as file:
                users = {}
                for line in file:
                    username, security = line.strip().split(":")
                    users[int(username)] = {"security": security}
                return users
        except FileNotFoundError:
            return {}

    def save_users(self):
        with open("accounts.txt", "w") as file:
            for username, user in self.users.items():
                file.write(f"{username}:{user['security']}\n")

    def register(self):
        username = random.randint(1000, 9999)
        security = input("Create Security: ")
        self.users[username] = {"security": security}
        self.save_users()
        print("Your username is: ", username)

    def get_user(self, username):
        return self.users.get(username)

    def login(self, username, security):
        user = self.get_user(username)
        if user and user["security"] == security:
            print("Login successful!")
            return True
        else:
            print("Invalid username or security")
            return False

    def change_security(self, username, old_security, new_security):
        user = self.get_user(username)
        if user and user["security"] == old_security:
            user["security"] = new_security
            self.save_users()
            print("security changed successfully!")
        else:
            print("Invalid username or security")

def main():
    store = Store()
    while True:
        choice = input("3nter y0ur ch01c3:\n1. R3g1st3r\n2. L06 1n\n3. Ch4ng3 S3cur1ty\n4. 3ND\n")
        if choice == "1":
            store.register()
        elif choice == "2":
            username = int(input("Enter your username: "))
            security = input("Enter your security: ")
            if store.login(username, security):
                print("You are logged in!")
            else:
                print("Login failed")
        elif choice == "3":
            username = int(input("Enter your username: "))
            old_security = input("Enter your old security: ")
            new_security = input("Enter your new security: ")
            store.change_security(username, old_security, new_security)
        elif choice == "4":
            print("Thank you!")
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()
