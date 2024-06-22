# Import the necessary NLTK library
import nltk
# Download the “book” collection from nltk
nltk.download("book")
# Import text1 from the nltk book collection
from nltk.book import text1

# Display the collocations found in text1
text1.collocations()
