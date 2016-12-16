import tweepy
import textblob
import ConfigParser

#config file to get twitter developer info
configParser = ConfigParser.RawConfigParser()
configFilePath = 'twitterConfig.txt'
configParser.read(configFilePath)

consumer_key = configParser.get('twitter', 'consumer_key')
consumer_secret = configParser.get('twitter', 'consumer_secret')

access_token = configParser.get('twitter', 'access_token')
access_token_secret = configParser.get('twitter', 'access_token_secret')

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#set queries
public_tweets = api.search(q="cat", count = 100)

#print polarity and subjectivity for each tweet
for tweet in public_tweets:
    print(tweet.text)
    print(textblob.TextBlob(tweet.text).sentiment)