# Write a program to count the total number of characters in a text file, including spaces. 

file = open("student.txt", "r")
text = file.read()
count = len(text)
print("Total number of characters (including spaces):", count)
file.close()
