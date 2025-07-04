import tweepy, os, datetime
import google.generativeai as genai

# Authenticate with X
auth = tweepy.OAuth1UserHandler(
    os.environ['CONSUMER_KEY'],
    os.environ['CONSUMER_SECRET'],
    os.environ['ACCESS_TOKEN'],
    os.environ['ACCESS_SECRET']
)
api = tweepy.API(auth)

# Authenticate with Gemini
genai.configure(api_key=os.environ['GEMINI_API_KEY'])
model = genai.GenerativeModel(model_name="models/gemini-pro")

# Generate tweet content
try:
    prompt = f"Generate a short tweet under 280 characters for {datetime.date.today()}, about data analytics or productivity."
    response = model.generate_content(prompt)
    print("Gemini says:", response.text)

    tweet = response.text.strip()
    api.update_status(tweet)

except Exception as e:
    print(f"Error occurred: {e}")
