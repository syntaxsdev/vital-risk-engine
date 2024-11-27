from .base import BrokerBase, T

from alpaca.trading.client import TradingClient
from alpaca.data.live import StockDataStream
from alpaca.common.exceptions import APIError
from typing import TypeVar, Awaitable, Callable

import os
import asyncio


async def alpaca_wrapper(func: Callable[..., T], *args, **kwargs) -> T:
    """Wraps Alpaca API into async requests

    Args:
        func: the Alpaca resource function
        *args: Additional position arguments for the request function
        **kwargs: Keyword arguments for the request function

    Returns:
        T: The response from the Alpaca API request
    """
    try:
        return await asyncio.to_thread(func(*args, **kwargs))
    except APIError:
        return None


class Alpaca(BrokerBase):
    def __init__(self, paper: bool = False):
        alpaca_key = os.getenv("ALPACA_API_KEY")
        alpaca_api_secret = os.getenv("ALPACA_API_SECRET")
        alpaca_paper_api_key = os.getenv("ALPACA_PAPER_API_SECRET")
        alpaca_paper_api_secret = os.getenv("ALPACA_PAPER_API_SECRET")

        api_key = None
        api_secret = None
        if paper:
            api_key = alpaca_paper_api_key
            api_secret = alpaca_paper_api_secret
        else:
            api_key = alpaca_key
            api_secret = alpaca_api_secret

        if not api_key:
            raise EnvironmentError("Alpaca API Key not set.")

        if not api_secret:
            raise EnvironmentError("Alpaca API Secret not set.")

        # Create the Alpaca Client
        self.client = TradingClient(
            api_key=api_key, secret=api_secret, paper=paper
        )

        # Create Stock Stream Client
        self.stream = StockDataStream(api_key=api_key, secret_key=api_secret)

    async def get_positions(self):
        """Get list of positions"""
        positions = await alpaca_wrapper(self.client.get_all_positions) or []
        return positions
