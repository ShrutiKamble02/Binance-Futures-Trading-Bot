import os

from dotenv import load_dotenv
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException

from bot.logging_config import setup_logger

# Load environment variables
load_dotenv()

logger = setup_logger()


class BinanceClient:
    def __init__(self):
        self.api_key = os.getenv("BINANCE_API_KEY")
        self.api_secret = os.getenv("BINANCE_API_SECRET")

        if not self.api_key or not self.api_secret:
            raise ValueError(
                "API Key or Secret Key not found. Please check your .env file."
            )

        # Initialize Binance Client for Testnet
        self.client = Client(
            api_key=self.api_key,
            api_secret=self.api_secret,
            testnet=True
        )

    def get_client(self):
        """
        Test the connection and return the authenticated client.
        """
        try:
            # Verify connection
            self.client.futures_ping()

            logger.info("Connected to Binance Futures Testnet successfully.")

            return self.client

        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e}")
            raise

        except BinanceRequestException as e:
            logger.error(f"Network Error: {e}")
            raise

        except Exception as e:
            logger.error(f"Unexpected Error: {e}")
            raise