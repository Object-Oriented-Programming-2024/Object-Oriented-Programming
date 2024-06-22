import pandas as pd
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import re
import gensim
from gensim import corpora

# Download necessary NLTK resources
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

class NLPTweets:
 """A class to apply NLP techniques on Tweets"""

 # Storing the dataframe and the column for processing the tweets
 def __init__(self, df,col_name):
     self.df= df # DataFrame containing the tweets
     self.col_name=col_name # Column name with the tweets
     self.processed_tweets=[] # List of pre-processed tweets

 def pre_process_tweets(self):

     # Dropping rows with null values in the column with tweets
     self.df.dropna(subset=[self.col_name], inplace=True)

     # The column with textual data
     tweets = self.df[self.col_name].values

     for tweet in tweets:
         # Using stopwords from the english dictionary to remove
         stop_words = set(stopwords.words('english'))

         #Using a Lemmatizer to find and replace with root words
         lemmatizer = WordNetLemmatizer()

         # Using pattern matching to remove noise from the data
         tweet = re.sub(r"#\w+", "", tweet) # Removing any  hastags
         tweet = re.sub(r"@\w+", "", tweet)  # Removing mentions
         tweet = re.sub(r"https?://\S+|www\.\S+","",tweet)  # Removing URLs
         tweet = re.sub(r"\d+", "", tweet) # Removing numbers such as a date
         tweet=''.join([char for char in tweet if char not in string.punctuation])

         # Tokenizing and and Lemmatizing each tweet
         words = word_tokenize(tweet)
         words = [
              lemmatizer.lemmatize(word)
              for word in words
              if word not in stop_words ]

         #Adding the processed tweets to a list
         self.processed_tweets.append(words)

     return self.processed_tweets

 def vectorize_tweets(self):

     # Creating a dictionary of unique words from tweets, each given an integer value
     self.dictionary = corpora.Dictionary(self.processed_tweets)

     # Bag of words strategy, each word as integer its frequency in the tweet
     self.corpus = [self.dictionary.doc2bow(text) for text in self.processed_tweets]

     return self.corpus


 def apply_topic_modelling(self,num_topics):

     # applying LDA
     lda_model = gensim.models.LdaModel(
         self.corpus,
         num_topics=num_topics,
         id2word=self.dictionary, passes=10)

     # Retrieving the topics
     topics = lda_model.print_topics(num_words=6)
     return topics


# Retrieving the dataset
df = pd.read_csv(
   "https://raw.githubusercontent.com/Object-Oriented-Programming-2024/"  \
   "Object-Oriented-Programming/main/Chapter9/newyear_resolutions.csv"
)

nlp_tweets=NLPTweets(df,"text") #Creating the NLPTweets Instance
processed_tweets=nlp_tweets.pre_process_tweets()

corpus=nlp_tweets.vectorize_tweets()

topics = nlp_tweets.apply_topic_modelling(5)
for topic in topics:
 print(topic)
