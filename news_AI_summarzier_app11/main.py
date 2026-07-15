import os
import time
import requests
from dotenv import load_dotenv
from google import genai
from send_email import send_email

# Load .env
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

if not GOOGLE_API_KEY:
    raise Exception("GOOGLE_API_KEY not found in .env")

if not NEWS_API_KEY:
    raise Exception("NEWS_API_KEY not found in .env")

client = genai.Client(api_key=GOOGLE_API_KEY)

url = (
    "https://newsapi.org/v2/top-headlines?"
    f"category=business&"
    f"language=en&"
    f"pageSize=8&"
    f"apiKey={NEWS_API_KEY}"
)

print("Fetching latest news...")

response = requests.get(url)

if response.status_code != 200:
    raise Exception(response.text)

data = response.json()

if data["status"] != "ok":
    raise Exception(data)

articles = data["articles"]

headlines = ""

print("\nToday's Business Headlines:\n")

for article in articles:
    title = article.get("title", "")
    print("•", title)
    headlines += f"- {title}\n"

headlines = "\n".join(
    article["title"] for article in articles if article.get("title")
)

prompt = f"""
Summarize these business news headlines in about 150 words.

Then explain in 80-100 words how these headlines might affect today's stock market.

Headlines:
{headlines}
"""

print("\nGenerating AI summary...\n")

MODELS = [
    "gemini-3.1-flash-lite",
    "gemini-2.0-flash-lite",
    "gemini-2.0-flash"
]

summary = None

for model in MODELS:

    print(f"Trying model: {model}")

    for attempt in range(3):

        try:

            result = client.models.generate_content(
                model=model,
                contents=prompt
            )

            summary = result.text

            print("\nAI Summary Generated Successfully!\n")
            break

        except Exception as e:

            print(f"Attempt {attempt+1} failed.")
            print(e)

            if attempt < 2:
                print("Retrying in 5 seconds...\n")
                time.sleep(5)

    if summary:
        break

if summary is None:
    raise Exception(
        "All Gemini models are currently unavailable. Please try again later."
    )

print(summary)

send_email(summary)

print("\nEmail sent successfully!")