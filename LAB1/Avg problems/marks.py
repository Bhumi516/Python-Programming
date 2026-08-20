marks=float(input("Enter your percentage: "))
if(marks>=90):
    print("Excellent Performance")
elif(marks>=80 and marks<=90):
    print("Very good performance") 
elif(marks>=70 and marks<=80):
    print("Good Performance")
elif(marks>=60 and marks<=70):
    print("Average Performance")
elif(marks>=50 and marks<=60):
    print("Improve your performance")
else:
    print("Too bad...Need to improve a lot")