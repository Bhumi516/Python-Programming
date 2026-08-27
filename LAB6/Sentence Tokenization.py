import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')

text = "Hello. How are you? I am fine."

sentences = sent_tokenize(text)

print(sentences)