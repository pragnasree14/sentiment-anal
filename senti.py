import tweepy
from textblob import TextBlob
consumer_key = ''#you get from twitter API
consumer_secret = ''#you get from twitter API
access_token = ''#you get from twitter API
access_token_secret = ''#you get from twitter API
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api=tweepy.API(auth)
public_tweets = api.search('Mahesh Babu')
for tweet in public_tweets:
  print(tweet.text)
  analysis=TextBlob(tweet.text)
  print(analysis.sentiment)
