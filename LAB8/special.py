# Read a text file and calculate the number of alphabets, digits, spaces, and special characters. 

file = open("student.txt", "r")
text = file.read()
alphabets = 0
digits = 0
spaces = 0
special_characters = 0
for char in text:
    if char.isalpha():
        alphabets += 1
    elif char.isdigit():
        digits += 1
    elif char.isspace():
        spaces += 1
    else:
        special_characters += 1
        
print("Total number of alphabets:", alphabets)
print("Total number of digits:", digits)        
print("Total number of spaces:", spaces)
print("Total number of special characters:", special_characters)
file.close()
