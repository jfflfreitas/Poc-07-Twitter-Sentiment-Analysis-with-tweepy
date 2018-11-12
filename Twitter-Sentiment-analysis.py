from textblob import TextBlob as tb
import tweepy
import numpy as np

#Setting up the  twitter app credentials. for more information access: developer.twitter.com and create an app.
consumer_key = 'YOUR CONSUMER KEY'
consumer_secret = 'YOUR CONSUMER SECRET'
accsess_token = 'YOUR ACCESS TOKEN'
accsess_token_secret = 'YOUR ACCESS TOKEN SECRET'

#Creating variables to make the authentication using the tweepy library
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(accsess_token, accsess_token_secret)
api = tweepy.API(auth)

#Variable that will store all Tweets with the chosen word in the API search function

public_tweets = api.search('Trump')

#Variable that will store the polarities about the tweets.
analysis = None

#Creating a empty list to store the scores.
tweets = []

#Loop to print all the tweets and then the polarity
for tweet in public_tweets:
    print(tweet.text)
    analysis = tb(tweet.text)
    polarity = analysis.sentiment.polarity
    tweets.append(polarity)
    print(polarity)

#Creating an average calculation of all tweets returned using the numpy mean function.
print('Média de Sentimento: ' + str(np.mean(tweets)))