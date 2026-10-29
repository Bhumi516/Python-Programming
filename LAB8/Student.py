#  Write a Python program to create a file named student.txt and write the student's name, 
#  roll number, branch, and semester into the file. 


file = open("student.txt", "w")
file.write("Name: Bhumi\n")
file.write("Roll Number: 12345\n")
file.write("Branch: Computer Science\n")
file.write("Semester: 5\n")
file.close()
