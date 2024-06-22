# Import the necessary modules from the nltk library
import nltk
from nltk.tokenize import word_tokenize

# Download the ‘averaged_perceptron_tagger’ resource from nltk
nltk.download('averaged_perceptron_tagger')

# Define the text
text = "Michael Jordan was born in Brooklyn, New York, and he became a "\
       "renowned professional basketball player."

# Tokenize the text into individual words
tokens = word_tokenize(text)

# Perform part-of-speech tagging on the tokenized words
tags = nltk.pos_tag(tokens)

# Print the list of words with their corresponding part-of-speech tag
print("Tags:",tags)
