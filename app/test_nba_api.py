import time
from app.nba_api_utils import *
import openai
from app.config import OPENAI_API_KEY
from openai import OpenAI
from openai import RateLimitError

def test_nba_api():
    openai.api_key = OPENAI_API_KEY
    client = OpenAI(api_key=OPENAI_API_KEY)

    max_retries = 5  # Number of times to retry if rate-limited
    delay = 1  # Initial delay in seconds

    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": "Who won the NBA Finals in 2016?"}],
                max_tokens=50  # Reduce token usage to save credits
            )
            print(response.choices[0].message.content)
            return  # Exit function after a successful request

        except RateLimitError:
            print(f"Rate limit reached. Retrying in {delay} seconds...")
            time.sleep(delay)
            delay *= 2  # Exponential backoff (1s → 2s → 4s → 8s → 16s)

    print("Request failed after multiple attempts. Please try again later.")




if __name__ == "__main__":
    test_nba_api()