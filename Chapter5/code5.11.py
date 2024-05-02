class Blog: # Class that defines a Blog
 def __init__(self):
     self.followers = [] # Initialize an empty list to store followers

 def add_follower(self, follower): # Method to add a follower to the blog
     self.followers.append(follower)

 def remove_follower(self, follower): # Method to remove a follower to the blog
     self.followers.remove(follower)

 def publish_post(self, title, topic): # Method to publish a post and notify followers
     for f in self.followers:
         f.new_post(title, topic)


class Follower: # Class that defines a Follower
 def __init__(self, name, interests): # Initialize a Follower Instance
     self.name = name
     self.interests = interests

 def new_post(self, title, topic): # Notify a follower about a new post
     if topic in self.interests:
         print(f"User {self.name} notified about new article: {title}")


#Creating a Blog
myBlog = Blog()

# Create followers of the Blog
follower1 = Follower("Imran Ali", ["Research", "AI"])
follower2 = Follower("Ibrahim Farooq", ["Education", "Politics"])

# Registering followers
myBlog.add_follower(follower1)
myBlog.add_follower(follower2)

# Publish posts
myBlog.publish_post("Bias in AI", "AI")
myBlog.publish_post("Upcoming elections", "Politics")
