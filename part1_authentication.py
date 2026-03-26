import os
from part2_encryption import apply_encryption, apply_decryption, encrypt, decrypt

FILE_NAME = "users.txt"
MAX_ATTEMPTS = 4

def is_valid_username(username):
    return username.isalpha() and len(username) >= 4

def is_valid_password(password):
    if len(password) < 9:
        return False
    
    upper = sum(1 for c in password if c.isupper())
    digit = sum(1 for c in password if c.isdigit())
    special = sum(1 for c in password if not c.isalnum())

    return upper >= 2 and digit >= 1 and special >= 2

def load_users():
    users = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            for line in f:
                enc_user, enc_pass = line.strip().split(",")
                
                user = decrypt(enc_user)
                pwd = apply_decryption(user, enc_pass)
                
                users[user] = pwd
    return users

def save_user(username, password):
    enc_user = encrypt(username)
    enc_pass = apply_encryption(username, password)
    
    with open(FILE_NAME, "a") as f:
        f.write(f"{enc_user},{enc_pass}\n")

def create_user():
    while True:
        username = input("Enter username: ")
        if not is_valid_username(username):
            print("Invalid username.")
            continue

        password = input("Enter password: ")
        if not is_valid_password(password):
            print("Invalid password.")
            continue

        save_user(username, password)
        print("User created!")
        break

def login():
    users = load_users()
    attempts = 0

    while attempts < MAX_ATTEMPTS:
        username = input("Username: ")
        password = input("Password: ")

        if username in users and users[username] == password:
            print("Login successful!")
            return
        else:
            attempts += 1
            print("Wrong login.")

    print("System is Locked.")

def reset_password():
    users = load_users()
    attempts = 0

    while attempts < 3:
        username = input("Enter username: ")
        if username in users:
            new_password = input("Enter new password: ")
            users[username] = new_password

            with open(FILE_NAME, "w") as f:
                for u, p in users.items():
                    enc_user = encrypt(u)
                    enc_pass = apply_encryption(u, p)
                    f.write(f"{enc_user},{enc_pass}\n")

            print("Password reset!")
            return
        else:
            attempts += 1
            print("User not found.")

def menu():
    while True:
        print("\n1. Create User\n2. Login\n3. Reset Password\n4. Exit")
        choice = input("Choose: ")

        if choice == "1":
            create_user()
        elif choice == "2":
            login()
        elif choice == "3":
            reset_password()
        elif choice == "4":
            break
        else:
            print("Invalid choice")

menu()