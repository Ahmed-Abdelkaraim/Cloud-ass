import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('punkt')
from collections import Counter
content = ""
with open("paragraphs.txt", "r") as file:
    content = file.read()
    word_tokens = word_tokenize(content)

word_tokens = word_tokenize(content)
stop_words = set(stopwords.words("english"))
filtered_text = [
    word for word in word_tokens if word.isalpha() and word.lower() not in stop_words
]

word_freq = Counter(filtered_text)
for word, freq in word_freq.most_common(100):
    print(f"{word}:{freq}")
