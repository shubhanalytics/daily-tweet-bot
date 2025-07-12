import os
import random
import tweepy

# --- Twitter Authentication ---
auth = tweepy.OAuth1UserHandler(
    os.environ['CONSUMER_KEY'],
    os.environ['CONSUMER_SECRET'],
    os.environ['ACCESS_TOKEN'],
    os.environ['ACCESS_SECRET']
)
api = tweepy.API(auth)

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

# --- Pick Random Tweet ---
tweet_text = random.choice(lines)
print("📢 Tweet selected:", tweet_text)

# --- Post Tweet ---
try:
    response = api.update_status(tweet_text)
    print("✅ Tweet posted successfully. Tweet ID:", response.id)
except Exception as e:
    print("❌ Error posting tweet:", e)
    exit(1)
