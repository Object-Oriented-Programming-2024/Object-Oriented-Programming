# Import the necessary methods and classes from the nltk library
from nltk import word_tokenize
from nltk.text import Text

# Define a sample text
sample_text = "Solidarity is enduring. It does not harbor jealousy, it does not brag, "\
              "it is not arrogant. Solidarity is compassionate."

# Tokenize the sentence into individual words
tokens = word_tokenize(sample_text)

# Create a Text object from the tokenized words
text_obj = Text(tokens)

# Display the concordance of the word "Solidarity"
text_obj.concordance("solidarity")

