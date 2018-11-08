# for interpreter use to test textblob
#from textblob import TextBlob
#
#wiki = TextBlob("Matie is angry that he never gets goot matches on Tinder")
#wiki.tags
#wiki.words
#wiki.sentiment.polarity

import tweetpy
from textblob import TextBlob as TB 

# Api keys to connect to the twitter API
consumer_key = 'ElOVheQZ5EixJ92d8spajZ7QT'
consumer_secret = '6MWE1vKpAlpiNK96VG4xeqyJWxfvXnNideCAYZNDVx6iN9Hthz'

# access tokens to gain rw access through authentication
access_token = '2895786628-TyGpy0Ffrs6uhfOgOyuMtbHmsKxFfuO12tGP51Y'
access_token_secret = 'py2ql1fWqnSJjGSTr6h09ytbeKGJcd5BK7ihWySG46RoP'

# Auth variable to handle API handshake and Auth access with twitter
auth = tweetpy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# API connection object
api = tweetpy.API(auth)

# variable to search for tweets that contain a specific term
public_tweets = api.search('feet')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)

