# ●	Check whether the entered string is a palindrome. 

word=input("Enter the word: ")
rev=word[::-1]
if(word== rev):
    print("Palindrome")
else:
    print("Not Palindrome")