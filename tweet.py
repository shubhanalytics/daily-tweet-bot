import requests, os, datetime
import tweepy
import time

# Twitter Auth
auth = tweepy.OAuth1UserHandler(
    os.environ['CONSUMER_KEY'],
    os.environ['CONSUMER_SECRET'],
    os.environ['ACCESS_TOKEN'],
    os.environ['ACCESS_SECRET']
)
api = tweepy.API(auth)

# Gemini REST API Call
GEMINI_API_KEY = os.environ['GEMINI_API_KEY']
API_URL = "https://generativelanguage.googleapis.com/v1/models/gemini-1.5-pro:generateContent"

prompt = f"Generate a short tweet under 280 characters for {datetime.date.today()} about data analytics, productivity, or growth mindset."

payload = {
    "contents": [
        {"parts": [{"text": prompt}]}
    ]
}
# Retry setup for Gemini API
session = requests.Session()
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

retry_strategy = Retry(
    total=5,
    backoff_factor=2,
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["POST"]
)
adapter = HTTPAdapter(max_retries=retry_strategy)
session.mount("https://", adapter)

try:
    print("⏳ Waiting before sending the Gemini API request...")
    time.sleep(5)  # ⬅️ Throttle delay to avoid hitting rate limits

    response = session.post ( f"{API_URL}?key={GEMINI_API_KEY}" , json=payload )
    response.raise_for_status()
    gemini_text = response.json()['candidates'][0]['content']['parts'][0]['text'].strip()

    if len(gemini_text) > 280:
        print("❌ Gemini response too long:", len(gemini_text), "characters")
        exit(1)


    print("Gemini response:", gemini_text)
    response = api.update_status(gemini_text)
    print("Tweet posted with ID:", response.id)


except Exception as e:
    print("Error occurred while tweeting:", e)
    exit(1)  # ✅ This signals failure to GitHub Actions

