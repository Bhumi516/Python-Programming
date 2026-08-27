class Text:

    def __init__(self, sentence):
        self.sentence = sentence

    def sentence_token(self):
        print("Sentences:")
        print(self.sentence.split("."))

    def word_token(self):
        print("Words:")
        print(self.sentence.split())

    def stopword(self):
        stop = ["is", "a", "the", "and"]
        words = self.sentence.split()

        result = []
        for word in words:
            if word.lower() not in stop:
                result.append(word)

        print("After Stopword Removal:")
        print(result)


# Variable
text = "Python is a programming language. Python is easy and powerful."

# Object
obj = Text(text)

# Function calls
obj.sentence_token()
obj.word_token()
obj.stopword()