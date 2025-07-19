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
print("📣 Selected tweet:", tweet_text)

# --- Fetch Environment Variables ---
required_keys = [
    "TWITTER_CONSUMER_KEY",
    "TWITTER_CONSUMER_SECRET",
    "TWITTER_ACCESS_TOKEN",
    "TWITTER_ACCESS_TOKEN_SECRET"
]

missing = [k for k in required_keys if not os.getenv(k)]
if missing:
    print(f"🚨 Missing environment variables: {', '.join(missing)}")
    exit(1)

# --- Authenticate via OAuth1 ---
auth = tweepy.OAuth1UserHandler(
    os.getenv("TWITTER_CONSUMER_KEY"),
    os.getenv("TWITTER_CONSUMER_SECRET"),
    os.getenv("TWITTER_ACCESS_TOKEN"),
    os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
)

api = tweepy.API(auth)

# --- Post Tweet ---
try:
    response = api.update_status(status=tweet_text)
    tweet_id = response.id_str
    print(f"✅ Tweet posted at {datetime.now()}. Tweet ID: {tweet_id}")

    # --- Optional: Archive Tweet ---
    with open("archive.txt", "a", encoding="utf-8") as log:
        log.write(f"{datetime.now()}: {tweet_text} → {tweet_id}\n")

except Exception as e:
    print("❌ Error posting tweet:", e)
    exit(1)
