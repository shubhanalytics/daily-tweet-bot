import tweepy, os, datetime
import google.generativeai as genai

# X Auth
auth = tweepy.OAuth1UserHandler(
    os.environ['CONSUMER_KEY'],
    os.environ['CONSUMER_SECRET'],
    os.environ['ACCESS_TOKEN'],
    os.environ['ACCESS_SECRET']
)
api = tweepy.API(auth)

# Gemini Auth
genai.configure(api_key=os.environ['GEMINI_API_KEY'])
model = genai.GenerativeModel("gemini-pro")
response = model.generate_content(
    f"Generate a short tweet under 280 characters for {datetime.date.today()} about data analytics or productivity."
)


prompt = f"Generate a short tweet under 280 characters for {datetime.date.today()} about data analytics, productivity, or mindset. Make it catchy and professional."

try:
    response = chat.send_message(prompt)
    tweet = response.text.strip()
    print("Gemini responded with:", tweet)
    api.update_status(tweet)
except Exception as e:
    print(f"Error occurred while tweeting: {e}")
