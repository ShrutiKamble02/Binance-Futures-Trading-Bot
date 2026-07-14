import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_API_SECRET")

print("API Key loaded:", api_key is not None)
print("API Secret loaded:", api_secret is not None)

if api_key:
    print("API Key length:", len(api_key))

if api_secret:
    print("API Secret length:", len(api_secret))