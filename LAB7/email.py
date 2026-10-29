import re

def validate_email(email):
    pattern = r'^[\w.-]+@[\w.-]+\.\w+$'

    if re.match(pattern, email):
        return "Valid Email"
    else:
        return "Invalid Email"


email = input("Enter your email: ")

print(validate_email(email))

