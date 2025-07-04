import tweepy
import datetime
import os

# Authenticate securely via GitHub Secrets
auth = tweepy.OAuth1UserHandler(
    os.environ['CONSUMER_KEY'],
    os.environ['CONSUMER_SECRET'],
    os.environ['ACCESS_TOKEN'],
    os.environ['ACCESS_SECRET']
)
api = tweepy.API(auth)

# Compose and post tweet
tweet = f"Daily data tip for {datetime.datetime.now().strftime('%Y-%m-%d')}: Always visualize your distributions!"
api.update_status(tweet)
