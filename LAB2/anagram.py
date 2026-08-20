# a.	Check whether two strings are anagrams. 

str1=input("Enter a 1st word: ")
str2=input("Enter a 2nd word: ")

if sorted(str1) == sorted(str2):
    print("Anagram")
else:
    print("Not anagram")
    