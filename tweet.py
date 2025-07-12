import os
import random
import tweepy
from datetime import datetime

# --- Load Tweets from File ---
try:
    with open("tweets.txt", "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
except Exception as e:
    print("❌ Failed to load tweets.txt:", e)
    exit(1)

if not lines:
    print("⚠️ tweets.txt is empty. Add some lines and retry.")
    exit(1)

# --- Select Random Tweet ---
tweet_text = random.choice(lines)
print("📢 Selected tweet:", tweet_text)

# --- Twitter API Authentication (OAuth2)
client = tweepy.Client(
    bearer_token=os.environ['TWITTER_BEARER_TOKEN'],
    consumer_key=os.environ['TWITTER_CLIENT_ID'],
    consumer_secret=os.environ['TWITTER_CLIENT_SECRET'],
    access_token=os.environ['TWITTER_ACCESS_TOKEN'],
    access_token_secret=os.environ['TWITTER_ACCESS_SECRET']
)

# --- Post Tweet via API v2 ---
try:
    response = client.create_tweet(text=tweet_text)
    tweet_id = response.data['id']
    print(f"✅ Tweet posted successfully at {datetime.now()}. Tweet ID: {tweet_id}")

    # Optional: archive tweet
    with open("archive.txt", "a", encoding="utf-8") as log:
        log.write(f"{datetime.now()}: {tweet_text} → {tweet_id}\n")

except Exception as e:
    print("❌ Error posting tweet:", e)
    exit(1)
