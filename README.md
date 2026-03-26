README – User Authentication & Encryption Project

Project Overview

This Python project is a secure user authentication system that allows users to:

Create an account with a strong username and password
Log in with their credentials
Reset their password if needed

The system encrypts usernames and passwords before storing them in a file (users.txt) to improve security.

Files Included
part1_authentication.py – Main program with menu, user creation, login, and password reset
part2_encryption.py – Encryption and decryption functions used to protect usernames and passwords
users.txt – Stores the encrypted user credentials

How to Run
Make sure Python 3 is installed on your computer.
Place all files in the same folder.
Open a terminal (or command prompt) in that folder.

Run the program:
python part1_authentication.py
Follow the on-screen menu to:
Create a new user
Log in
Reset a password
Exit the program
Username & Password Rules
Username
At least 4 alphabetic characters
No numbers, symbols, or spaces
Password
Minimum 9 characters
At least 2 uppercase letters
At least 1 number
At least 2 special characters (e.g., !, @, #, $)
Encryption Method
Usernames and passwords are stored encrypted in users.txt.
Encryption uses a transposition cipher:
Username length even → single encryption
Username length odd → double encryption
Decryption is applied during login to validate credentials.
Features Demonstrated
User input validation
Secure login system
Password reset functionality
Encrypted storage of sensitive data
Notes
Make sure users.txt is in the same folder as the Python files.
The program locks after 4 consecutive failed login attempts to protect against unauthorized access.
The password reset function allows 3 attempts to enter a valid username before returning to the main menu.

Author

Ortasele Aisuan

Course: CST 535 – Principles of Computer Security

Date: March 2026