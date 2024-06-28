import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.probability import FreqDist

df = pd.read_csv('customer_reviews.csv') # Load the customer review dataset
# View the column information
print(df.info())
review_texts = df['Review Text'].tolist() # Extract text and store it into a list

def tokenize_text(text):
    """Tokenize the input text."""
    return word_tokenize(text)

def normalize_text(tokens):
    """Normalize text by converting to lowercase and remove stopwords."""
    tokens = [token.lower() for token in tokens if token.isalpha()]
    stop_words = set(stopwords.words('english'))
    return [token for token in tokens if token not in stop_words]

def tag_tokens(tokens):
     """Tag tokens with their parts of speech."""
     return nltk.pos_tag(tokens)

def get_sentiment(text):
    """Analyze the sentiment of the input text."""
    sia = SentimentIntensityAnalyzer()
    return sia.polarity_scores(text)

for text in review_texts:
    # Tokenize the input text
    tokens = tokenize_text(text)
    print(f"Tokens: {tokens}")

# Normalize the tokens
normalized_tokens = normalize_text(tokens)
print(f"Normalized Tokens: {normalized_tokens}")

# Apply Parts-of-Speech Tagging
pos_tags = tag_tokens(normalized_tokens)
print(f"POS Tags: {pos_tags}")

# Apply Frequency Distribution
freq_dist = FreqDist(normalized_tokens)
print("Most Common Words:", freq_dist.most_common(10))

# Apply Sentiment Analysis
sentiment = get_sentiment(text)
print(f"Sentiment: {sentiment}\n")
