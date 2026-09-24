import re

def validate_mobile(number):
    pattern = r'^[6-9][0-9]{9}$'

    if re.match(pattern, number):
        print("Valid Mobile Number")
    else:
        print("Invalid Mobile Number")


num = input("Enter mobile number: ")
validate_mobile(num)