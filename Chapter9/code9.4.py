# Import nltk library, work_tokenize and stopwords
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download the ‘stopwords’ data package from nltk, if not already downloaded
nltk.download('stopwords')

# Define a sample text
text = "This is an Example Sentence"

# Create a set of English stopwords
stop_words = set(stopwords.words('english'))

# Tokenize the text into individual words
tokens = word_tokenize(text)

# Filter out the stopwords from the tokenized words
filtered_text = [word for word in tokens if not word.lower() in stop_words]

# Print the filtered text, which excludes the stopwords
print(filtered_text)
