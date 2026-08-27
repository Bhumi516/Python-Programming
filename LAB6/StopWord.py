import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')

text = "This is a simple example of stopword removal."

words = word_tokenize(text)
stop_words = set(stopwords.words('english'))

result = [word for word in words if word.lower() not in stop_words]

print(result)