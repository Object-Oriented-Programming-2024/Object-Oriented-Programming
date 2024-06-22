# Import the necessary libraries and modules
import pylab, nltk
from nltk.probability import FreqDist
# Download the “book” collection from nltk
nltk.download("book")
# Import text1 from the nltk book collection
from nltk.book import text1

# Create a frequency distribution of the words in text1
fdist = FreqDist(text1)

# Print the 20 most common words in a cumulative frequency plot
print(fdist.most_common(20))

# Show the plot
fdist.plot(20, cumulative=True)
