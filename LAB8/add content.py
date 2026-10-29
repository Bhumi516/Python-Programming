# Write a program to append additional student information to an existing file without deleting
# its previous contents. 


file = open("student.txt", "a")
file.write("Name: Prath\n")
file.write("Roll Number: 67890\n")
file.write("Branch: Electrical Engineering\n")
file.write("Semester: 3\n")
file.close()