import random
import string
import hashlib

n = 4

def user_reg(users):
    # Get data from the user
    username = input("Enter User Name: ")
    password = str(input("Enter Password: ").encode())
    gender = input("Enter your Gender (PII): ")

    # Pool of characters from which Salt is to be made (Using a-z, A-Z, and 0-9)
    characters = string.ascii_letters + string.digits

    # Using 'random' function to create a random salt of 8 digits
    salt = ''.join(random.choice(characters) for i in range(8))
    print("Salt for the user '" + username + "' is :" + salt)

    # Appending Salt to the password
    plaintext = password + salt

    hashedtext = plaintext

    # Hashing the password up to N number of times (N is defined as 4)
    for i in range(n):
        hashedtext = hashlib.sha256(hashedtext.encode()).hexdigest()
    print("Password and Salted Password and Hashed password : ",password,plaintext,hashedtext)

    # Storing the user data as variables
    users[username] = {
        'salt': salt,
        'hash': hashedtext,
        'gender': gender
    }

def login(users):
    login_username = input("Enter the username to login: ")
    login_password = str(input("Enter the password of the user: ").encode())

    if login_username in users:
        user_data = users[login_username]

        # Fetch salt of the user to be logged in and append it to the password of the user
        salt = user_data['salt']
        temp_var = login_password + salt

        # Hashing the password + salt up to N number of times (N is defined as 4)
        hashedtext2 = temp_var
        for i in range(n):
            hashedtext2 = hashlib.sha256(hashedtext2.encode()).hexdigest()

        # Comparing the newly hashed password with the hashed password from the variables
        if hashedtext2 == user_data['hash']:
            print("LOGIN SUCCESSFUL")
        else:
            print("LOGIN FAILED")
    else:
        print("User not found")

# Dictionary to store user data
user_data_dict = {}

# While loop to display options for login or sign up
loop_var = 0
while loop_var == 0:
    loop_var = int(input("Enter number (1 for user Registration, 2 for Login, 3 to quit): "))
    if loop_var == 1:
        user_reg(user_data_dict)
        loop_var = 0
    elif loop_var == 2:
        login(user_data_dict)
        loop_var = 0
    elif loop_var == 3:
        break