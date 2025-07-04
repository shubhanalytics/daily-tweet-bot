import tweepy
import datetime

# Authenticate
auth = tweepy.OAuth1UserHandler(
    consumer_key="your-consumer-key",
    consumer_secret="your-consumer-secret",
    access_token="your-access-token",
    access_token_secret="your-access-secret"
)
api = tweepy.API(auth)

# Compose and post tweet
tweet = f"Daily data tip for {datetime.datetime.now().strftime('%Y-%m-%d')}: Always visualize your distributions!"
api.update_status(tweet)
