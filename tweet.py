
# importing the module 
import tweepy 
  
# personal information 
consumer_key ="xxxxxxxxxxxxxxxx" #add relevant keys
consumer_secret ="xxxxxxxxxxxxxxxx"
access_token ="xxxxxxxxxxxxxxxx"
access_token_secret ="xxxxxxxxxxxxxxxx"
  
# authentication 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret) 
   
api = tweepy.API(auth) 
tweet ="Text part of the tweet" # toDo 
image_path ="path of the image" # toDo 
  
# to attach the media file 
status = api.update_with_media('pil_text.png' tweet)  
api.update_status(status = tweet) 
