# Write a program to count the total number of words present in a text file. 


file = open("student.txt", "r")
text = file.read()
words = text.split()
count = len(words)
print("Total number of words:", count)
file.close()