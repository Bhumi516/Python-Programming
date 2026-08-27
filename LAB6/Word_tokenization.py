import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')

text = "Hello, how are you?"
words = word_tokenize(text)

print(words)