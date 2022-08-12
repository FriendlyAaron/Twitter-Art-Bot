import tweepy
import time
import praw
import os
import urllib.request

# Authenticate to Twitter
consumer_key = os.environ ['consumer_key']
consumer_secret = os.environ ['consumer_secret']
key = os.environ ['key']
secret = os.environ ['secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

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


api = tweepy.API(auth)

def getSubmission ():
  try:
    for submission in subreddit.hot(limit=30):
      slink = submission.url 
      plink = submission.permalink
      author = str(submission.author)
      if not submission.stickied and not submission.is_self and not submission.over_18 and not submission.saved and slink.endswith (('png','.jpg','gif')):
        submission.save()
        stitle = submission.title 
        type_file = submission.url[-4:]
        file = stitle+type_file
        urllib.request.urlretrieve(slink,file)
        media = api.media_upload(file) 
        tweet(stitle,author,plink,media,file)
        break  
  except:
    os.remove(file)
    print ('Failed to retrieve submission data')
  finally:
    print ('Failed to retrieve submission data')




  

def tweet (stitle,author,plink,media,file): 
  try:    
    api.update_status('"'+stitle+'" by  /u/'+author+': reddit.com'+plink,media_ids =[media.media_id_string],)
    print ('Tweeted')
    os.remove(file)
    time.sleep(1800)
  except:
    print ('Failed to tweet')
    os.remove(file)
    getSubmission()


 


while True:
  getSubmission()
