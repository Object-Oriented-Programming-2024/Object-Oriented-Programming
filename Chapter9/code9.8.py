# Import the necessary methods and classes from the nltk library
from nltk import word_tokenize, pos_tag
from nltk.chunk import RegexpParser

# Define a sample text
sentence = "A swift auburn fox leaps over the dormant hound."

# Tokenize the sentence into individual words
tokens = word_tokenize(sentence)

# Perform part-of-speech tagging on the tokenized words
tagged_tokens = pos_tag(tokens)

# Define the grammar for noun phrase (NP) chunking
grammar = "NP: {<DT>?<JJ>*<NN>}"

# Create a RegexpParser object with the defined grammar
cp = RegexpParser(grammar)

# Parse the tagged tokens to identify noun phrases
chunked = cp.parse(tagged_tokens)

# Draw the chunked structure
chunked.draw()
