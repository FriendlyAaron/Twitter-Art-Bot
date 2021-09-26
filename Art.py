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


def tweet ():
  try:
    for submission in subreddit.hot(limit=30):
      slink = submission.url 
      plink = submission.permalink
      author = submission.author
      if not submission.stickied and not submission.is_self and not submission.over_18 and not submission.saved and slink.endswith (('png','.jpg')):
        submission.save()
        stitle = submission.title 
        type_file = submission.url[-4:]
        urllib.request.urlretrieve(slink,stitle+type_file)
        media = api.media_upload(stitle+type_file)     
        api.update_status('"'+stitle+'" by  /u/'+author.name+': reddit.com'+plink,media_ids =[media.media_id_string],)
        print ('Tweeted')
        os.remove(stitle+type_file)
        time.sleep(1800)
        break
  except:
    tweet()


while True:
  tweet()
