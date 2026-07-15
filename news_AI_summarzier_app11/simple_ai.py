from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

prompt = """
You are a news summarizer.

Summarize these headlines:

- Apple launches a new iPhone.
- Tesla stock rises.
- Microsoft invests in AI.

Explain how this could affect the stock market.
"""

response = client.models.generate_content(
    model="gemini-flash-latest",
    contents=prompt
)

print(response.text)