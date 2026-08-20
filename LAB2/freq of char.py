# ●	Find the number of times a specified character appears in a string. 

text=input("Enter a string: ")
n=input("Enter a char: ")
for i in text:
    if(i==n):
        count=text.count(n)
print(count)