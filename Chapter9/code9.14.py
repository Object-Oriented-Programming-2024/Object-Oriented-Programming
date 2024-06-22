# Import the tweepy library for Twitter API interaction
import tweepy
# Import twitter_credentials module containing API keys and tokens
import twitter_credentials


class TweetWriter(tweepy.Client):
 """Wrapper Class for posting tweets."""

 def __init__(self):
     super().__init__() # Initialize parent class
     self.client = None # Client to access Twitter
     self.auth = None # Authorization of consumer key

 # Create a client to post tweets
 def createClient(self):
     self.client = tweepy.Client(twitter_credentials.BEARER_TOKEN,
                                 twitter_credentials.API_KEY,
                                 twitter_credentials.API_KEY_SECRET,
                                 twitter_credentials.ACCESS_TOKEN,
                                 twitter_credentials.ACCESS_TOKEN_SECRET)

 # Create authentication for the client access
 def createAuth(self):
     self.auth = tweepy.OAuthHandler(twitter_credentials.API_KEY,
                                     twitter_credentials.API_KEY_SECRET,
                                     twitter_credentials.ACCESS_TOKEN,
                                     twitter_credentials.ACCESS_TOKEN_SECRET)

 # Post a tweet on Twitter
 def writePost(self, post):
     self.client.create_tweet(text=post)

 # Reply to a post on Twitter
 def replyPost(self, tweetid, reply):
     self.client.create_tweet(in_reply_to_tweet_id=tweetid, text=reply)

# Create TweetWriter object and post a tweet
mytweeter = TweetWriter()
mytweeter.createClient()
mytweeter.createAuth()
mytweeter.writePost("This is a new post")
