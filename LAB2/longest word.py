text=input("Enter the string: ")
words=text.split()
longest=words[0]
for word in words:
    if len(word) > len(longest):
        longest=word
        
print("Longest word: ", longest)
print("Length: ", len(longest))
