import tweepy, os, datetime
import google.generativeai as genai

auth = tweepy.OAuth1UserHandler(
    os.environ['CONSUMER_KEY'],
    os.environ['CONSUMER_SECRET'],
    os.environ['ACCESS_TOKEN'],
    os.environ['ACCESS_SECRET']
)
api = tweepy.API(auth)

genai.configure(api_key=os.environ['GEMINI_API_KEY'])
model = genai.GenerativeModel("gemini-pro")

try:
    response = model.generate_content(
        f"Generate a tweet under 280 characters for {datetime.date.today()} about data analytics, productivity, or growth mindset."
    )
    tweet = response.text.strip()
    print("Gemini response:", tweet)
    api.update_status(tweet)
except Exception as e:
    print("Error occurred while tweeting:", e)
