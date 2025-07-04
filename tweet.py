import requests, os, datetime
import tweepy

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

try:
    response = requests.post(
        f"{API_URL}?key={GEMINI_API_KEY}",
        json=payload
    )
    response.raise_for_status()
    gemini_text = response.json()['candidates'][0]['content']['parts'][0]['text'].strip()

    print("Gemini response:", gemini_text)
    api.update_status(gemini_text)

except Exception as e:
    print("Error occurred while tweeting:", e)
