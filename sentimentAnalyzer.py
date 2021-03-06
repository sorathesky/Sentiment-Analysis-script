# for interpreter use to test textblob
#from textblob import TextBlob
#
#wiki = TextBlob("Matie is angry that he never gets goot matches on Tinder")
#wiki.tags
#wiki.words
#wiki.sentiment.polarity

import tweepy
from textblob import TextBlob as TB 
import csv


# Api keys to connect to the twitter API
consumer_key = 'xxxxx'
consumer_secret = 'xxxxx'

# access tokens to gain rw access through authentication
access_token = 'xxxx'
access_token_secret = 'xxx'

# Auth variable to handle API handshake and Auth access with twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# API connection object with limit rate 
api = tweepy.API(auth, wait_on_rate_limit=True)

# variable to search for tweets that contain a specific term
public_tweets = api.search('Pokemon')



#for tweet in public_tweets:
    #print(tweet.text)
    #analysis = TB(tweet.text)
    #print(analysis.sentiment)

with open("sentiment.csv",'w', encoding = 'utf-8-sig', newline='') as tf:
    writer = csv.writer(tf)

    for tweet in public_tweets:
        print(tweet.text)
        analysis = TB(tweet.text)
        print(analysis.sentiment)
        writer.writerow([tweet.text,analysis.sentiment])