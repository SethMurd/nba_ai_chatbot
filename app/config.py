import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Debugging: Print key to check if it's loading correctly (Remove in production)
print("OpenAI API Key:", OPENAI_API_KEY)  