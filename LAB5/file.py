file = open("student.txt", "w")

file.write("Name: Bhumi\n")
file.write("Course: CSE\n")
file.write("Year: Third")

file.close()

print("File created successfully")





file = open("student.txt", "r")

data = file.read()
print(data)

file.close()

print()






with open("student.txt", "r") as file:
    print(file.read())







