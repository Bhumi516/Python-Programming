text=input("Enter a string: ")
lower=0
upper=0
for i in text:
    if(i>='a' and i<='z'):
        lower+=1
    else:
        upper+=1
print("Lower: ",lower )
print("Upper: ",upper)