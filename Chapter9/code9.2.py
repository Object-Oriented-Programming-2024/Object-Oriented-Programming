# Import necessary libraries from NLTK for tokenization
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

# Define the text data
text = "Hello there! Welcome to the world of NLP."

# Tokenize the text into words
words = word_tokenize(text)

# Print word tokens
print("Word Tokens:")
print(words)

# Print sentence tokens
sentences = sent_tokenize(text)
print("Sentence Tokens:")
print(sentences)
