# a.	Check whether a given substring exists in the main string. 

str=input("Enter the string: ")
substr=input("Enter the substring: ")
if substr in str:
    print("Exist")
else:
    print("NOT exist")