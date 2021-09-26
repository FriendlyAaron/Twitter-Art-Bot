# Twitter-Art-Bot
This is a Twitter bot that tweets the most popular posts on [r/Art](https://www.reddit.com/r/Art/). Check the bot in action [here](https://twitter.com/Reddit_art_bot).

### Setup
###### Twitter App:
1. Create a [twitter](https://twitter.com/) account
2. [Navigate to the Apps page ](https://developer.twitter.com/en/portal/apps/21454677/settings)
3. Click *apply*
4. Submit and fill out all the info on the form.
5. Wait to be granted access.
6. Click *developer portal*
7. Click *Create project*
8. Note the outputted *API key*, *API secret*, *Access token* and *Access token secret*

###### Reddit App:
1. Create a [Reddit](https://www.reddit.com) account
2. [Navigate to the Apps page ](https://www.reddit.com/prefs/apps/)
3. Click *create an app*
4. **name:** Set a name for your app
5. **type:** Script
6. **description:** Optional
7. **about url:** Optional
8. **redirect url:** http://localhost
9. Note the outputted *client id* and *secret*

###### config py file:
1. **consumer_key:** your API key 
2. **consumer_secret:** your API secret
3. **key:** your Access token
4. **secret:** your Access token secret
5. **username:** your Reddit username
6. **password:** your Reddit password
7. **client_id:** the outputted client id
8. **client_secret:** the outputted secret
9. **reddit.subreddit:** Change the subreddit to any subreddit (Preferably one that has users post images)

######  Installtion
1. Download the latest python version from: https://www.python.org/downloads/
2. Download the Art.py file
3. Use pip3 to install praw in in terminal:         
         
         pip3 install praw
4. Use pip3 to install tweepy in in terminal:         
         
         pip3 install tweepy
5. Run the py file
6. Host the bot on any bot hosting platform to keep it online.  

## Gallery:
Some tweets the bot has made.

<img width="590" alt="Screen Shot 2021-09-26 at 3 00 53 PM" src="https://user-images.githubusercontent.com/84158176/134820742-712faede-45f0-479a-8716-a33bf77894e1.png">


<img width="593" alt="Screen Shot 2021-09-26 at 2 58 44 PM" src="https://user-images.githubusercontent.com/84158176/134820668-fdbb420f-326a-4ad4-9829-2993eceac404.png">

<img width="598" alt="Screen Shot 2021-09-26 at 2 59 24 PM" src="https://user-images.githubusercontent.com/84158176/134820688-ee84f6a4-b326-4921-ba91-e0ecbd8f5019.png">

