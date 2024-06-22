# Import the necessary libraries and modules
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Create an instance of the PorterStemmer
stemmer = PorterStemmer()

# Define a sample text
text = "Reading reads read"

# Tokenize the text into individual words
tokens = word_tokenize(text)

# Stem each tokenized word using the PorterStemmer
stemmed_words = [stemmer.stem(word) for word in tokens]

# Print the list of stemmed words
print(stemmed_words)
