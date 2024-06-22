# Import the necessary libraries
import pylab, nltk
# Download the 'book' collection from nltk
nltk.download("book")
# Import ‘text1’ from the nltk book collection
from nltk.book import text1

# Display the concordance for the word ‘ship’ in text1
text1.concordance("ship")

# Define a list of target words for the dispersion plot
target_words = ['ship', 'boat', 'vessel', 'craft']

# Generate a dispersion plot for the target dispersion plot
text1.dispersion_plot(target_words)

# Show the plot
pylab.show()
