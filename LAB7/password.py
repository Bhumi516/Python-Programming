import re

def check_password(password):

    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[@#$%^&*!]).{8,}$'

    if re.match(pattern, password):
        print("Strong Password")
    else:
        print("Weak Password")


password = input("Enter password: ")
check_password(password)