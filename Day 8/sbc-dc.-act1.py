# Dictionary to store user data
# File name to store user data
user_file = "users.txt"

def load_users():
    try:
        with open(user_file, 'r') as file:
            lines = file.readlines()
            users = {}
            for line in lines:
                username, password = line.strip().split(',')
                users[username] = password
            return users
    except FileNotFoundError:
        return {}

def save_users(users):
    with open(user_file, 'w') as file:
        for username, password in users.items():
            file.write(f"{username},{password}\n")

def register():
    users = load_users()
    username = input("Enter a username: ")
    if username in users:
        print("Username already exists. Please choose another one.")
        return
    
    password = input("Enter a password: ")
    users[username] = password
    save_users(users)
    print("Registration successful!")

def login():
    users = load_users()
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if username in users and users[username] == password:
        print("Login successful!")
    else:
        print("Login failed. Please check your username and password.")

def change_password():
    users = load_users()
    username = input("Enter your username: ")
    if username not in users:
        print("Username not found.")
        return
    
    current_password = input("Enter your current password: ")
    if users[username] != current_password:
        print("Current password is incorrect.")
        return
    
    new_password = input("Enter your new password: ")
    users[username] = new_password
    save_users(users)
    print("Password changed successfully!")

# Main loop to interact with the user
while True:
    print("\nhi. Register\nhello. Login\nwasap. Change Password\nmorning. Exit")
    choice = input("Enter your choice (hi,hello,wasap,morning): ")

    if choice == 'hi':
        register()
    elif choice == 'hello':
        login()
    elif choice == 'wasap':
        change_password()
    elif choice == 'morning':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter hi, hello, wasap, or morning.")
