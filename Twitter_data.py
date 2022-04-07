# from apiclient.discovery import build
import re
import tweepy
import datetime
import pandas as pd
import os


# Twitter_bits

CONSUMER_KEY = 'APLGGCEJCSoETuLCuXss3b3uK'
CONSUMER_SECRET = '2FoG0shCWewrjydt0qAqiRuPp7NrhzTBgASjpAMQdMEpQ4W3RQ'
ACCESS_KEY = '1300074870747795457-oc7sDMcYNOWwbdkjqUs92SzEuFGRy7'
ACCESS_SECRET = 'R6ohYaO2pBUtXDQlNb7PJRAAdGtuIoZ1ROUFLjLrSJ4Un'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

search_words = "#ad"


tweets = tweepy.Cursor(api.search, q=search_words+"-filter:retweets", until="2022-09-10",
                       lang="en", tweet_mode='extended').items(900)


users_locs = [[tweet.user.screen_name, tweet.full_text,
               tweet.created_at, ]for tweet in tweets]

'''for tweet in tweets:
    if tweet.favorite_count > 0:

        users_locs = [[tweet.user.screen_name, tweet.full_text,
                       tweet.favorite_count, tweet.user.location]]'''

tweet_text = pd.DataFrame(data=users_locs,
                          columns=['user', 'fulltext', 'date'])


tweet_text.to_csv("tweet_test.csv", index=False)
