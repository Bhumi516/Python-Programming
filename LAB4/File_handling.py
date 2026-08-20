# file=open("bhumi.txt","w") 
# file.write("Hello , how are you!!")


with open("bhumi.txt","w") as file:
    file.write("Hey\n")
    file.write("How are you?\n")
    file.write("Here's Bhumi\n")
    
    
    
with open("bhumi.txt","r") as file:
    data=file.read()
    print(data)
    
    
    
with open("bhumi.txt","r") as file:
    data=file.readline()
    print(data)
    
    

with open("bhumi.txt","r") as file:
    data=file.readlines()
    print(data)
    
    
    
with open("bhumi.txt","r") as file:
    for line in file:
        print(line.strip())
        


with open("bhumi.txt","a") as file:
    file.write("Hey i am fine..")
    file.write("This is Python Programming")
    


with open("bhumi.txt","w") as file:
    lines = [
        "First Line\n",
        "Second Line\n",
        "Third Line\n",
    ]
    file.writelines(lines)
    
    
    
with open("bhumi.txt","r") as file:
    data=file.read()
    print(data)
    
    

with open("bhumi.txt","r") as file:
    file.seek(6)
    print(file.read())
   
   

with open("bhumi.txt","w+") as file:
   file.write("Hello")
   file.seek(0)
   print(file.read())
    



with open("bhumi.txt","r+") as file:
    file.write("COllege\n")
    file.seek(0)
    print(file.read())
    
    


with open("bhumi.txt","a+") as file:
    file.write("Python")
    file.seek(0)
    print(file.read())