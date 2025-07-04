import tweepy, os, datetime
import google.generativeai as genai

try:
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
    model = genai.GenerativeModel('gemini-pro')

    # Generate tweet content
    # Generate tweet content
prompt = f"Generate a short tweet under 280 characters for {datetime.date.today()}, about data analytics or productivity."
response = model.generate_content(prompt)
print("Gemini raw response:", response)

try:
    tweet = response.text.strip()
    api.update_status(tweet)
except Exception as e:
    print(f"Error occurred while tweeting: {e}")
