# a.	Print all duplicate characters in a string. 

text= input("Enter the string: ")
for ch in set(text):
    if text.count(ch) > 1:
        print(ch, end=" ")