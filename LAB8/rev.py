# Write a program to read a text file and display its lines in reverse order. 

file = open("student.txt", "r")
text = file.readlines()
for line in reversed(text):
    print(line.strip())