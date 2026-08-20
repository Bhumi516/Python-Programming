text=input("Enter the string: ")
words=text.split()
shortest=words[0]
for word in words:
    if len(word) < len(shortest):
        shortest=word
        
print("Shortest word: ", shortest)
print("Length: ", len(shortest))
