import tweepy
import time
import praw
import os
import urllib.request


# Authenticate to Twitter
client = tweepy.Client(consumer_key = os.environ ['consumer_key'],
consumer_secret = os.environ ['consumer_secret'],
access_token = os.environ ['key'],
access_token_secret=  os.environ ['secret'])

consumer_key = os.environ ['consumer_key']
consumer_secret = os.environ ['consumer_secret']
key = os.environ ['key']
secret = os.environ ['secret']


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)



#Login to Reddit
reddit = praw.Reddit(
  client_id = os.environ ['client_id'],
  client_secret =os.environ ['client_secret'],
  username = os.environ ['username'],
  password =os.environ ['password'],
  user_agent = "Art"
)

#Set the subreddit
subreddit = reddit.subreddit("Art")



#Get Image from subreddit
def getSubmission ():
  try:
    for submission in subreddit.hot(limit=30):
      slink = submission.url 
      plink = submission.permalink
      author = str(submission.author)
      if not submission.stickied and not submission.is_self and not submission.saved and submission.over_18 and slink.endswith (('png','.jpg','gif','jpeg')):
        submission.save()
        stitle = submission.title 
        type_file = submission.url[-4:]
        file = stitle+type_file
        urllib.request.urlretrieve(slink,file)
        media = api.media_upload(file) 
        msg = '"'+stitle+'" posted by /u/'+author+': reddit.com'+plink
        tweet(msg,media,file)
        break  
  except Exception as e: 
    print ('Failed to retrieve submission data')
    print(e)

def tweet (msg,media,file): 
  try:     
    client.create_tweet(text=msg,media_ids =[media.media_id_string]) 
    print ('tweeted')
    os.remove(file)
    time.sleep(28800)
  except Exception as e:
    print ('Failed to tweet')
    print(e)
    

#keep_alive()
while True:
  getSubmission()
