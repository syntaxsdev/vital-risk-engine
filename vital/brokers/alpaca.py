from .base import BrokerBase
import os


class Alpaca(BrokerBase):
    def __init__(self, paper: bool = False):
        alpaca_key = os.getenv("ALPACA_API_KEY")
        alpaca_api_secret = os.getenv("ALPACA_API_SECRET")
        alpaca_paper_api_key = os.getenv("ALPACA_PAPER_API_SECRET")
        alpaca_paper_api_secret = os.getenv("ALPACA_PAPER_API_SECRET")

        if paper:
            self.api_key = alpaca_paper_api_key
            self.api_secret = alpaca_paper_api_secret
        else:
            self.api_key = alpaca_key
            self.api_secret = alpaca_api_secret

        if not self.api_key:
            raise EnvironmentError("Alpaca API Key not set.")

        if not self.api_secret:
            raise EnvironmentError("Alpaca API Secret not set.")
