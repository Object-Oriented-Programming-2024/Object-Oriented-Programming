# Import the necessary modules from the nltk library
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Download the ‘wordnet’ resource from nltk
nltk.download('wordnet')

# Create an instance of the WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

# Define a sample text
text = "I'm reading a reading read by a reader"

# Tokenize the text into individual words
tokens = word_tokenize(text)

# Lemmatize each tokenized word using the WordNetLemmatizer with part of speech as ‘verb’
lemmatized_words = [lemmatizer.lemmatize(word, pos='v') for word in tokens]

# Print the list of lemmatized words
print(lemmatized_words)
