# Read a text file and count the number of vowels and consonants present in the file. 

file = open("student.txt", "r")
text = file.read()
vowels = 0
consonants = 0
for char in text:
    if char.isalpha():
        if char.lower() in 'aeiou':
            vowels += 1
        else:
            consonants += 1
            
print("Total number of vowels:", vowels)
print("Total number of consonants:", consonants)
file.close()