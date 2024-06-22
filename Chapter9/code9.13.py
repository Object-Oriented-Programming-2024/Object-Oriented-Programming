# Import the SentimentIntensityAnalyzer class from the nltk.sentiment module
from nltk.sentiment import SentimentIntensityAnalyzer
# Import the NLTK library
import nltk

# Download the 'vader_lexicon' from NLTK, which is required for sentiment analysis
nltk.download('vader_lexicon')

# Create an instance of the SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

# Define a negative text for sentiment analysis
text_1= (
 "The service was absolutely horrendous, the staff was rude, and the entire "
 "experience was a complete disaster. I've never felt so unwelcome and "
 "disrespected in my life. Avoid this place at all costs; it's truly a nightmare."
)
text_2= (
 "The service was outstanding, the staff was incredibly friendly, and the whole "
 "experience was delightful. I've never felt so valued and well-treated."
 "Highly recommend this place; it’s absolutely wonderful!"
)
# Print the sentiment analysis scores for the negative text
print(sia.polarity_scores(text_1))
# Print the sentiment analysis scores for the positive text
print(sia.polarity_scores(text_2))
