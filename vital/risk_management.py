from .models import Profile
from vital.brokers import Alpaca

import asyncio

class RiskManagement:
    def __init__(self, broker: Alpaca, profile: Profile):
        """Create the RiskManagement service"""
        self.broker = broker
        self.profile = profile
        self.risk_mgmt = profile.risk_management

    async def start(self):
        """Start the RiskManagment service"""
        if not self.risk_mgmt.enabled:
            return

        await asyncio.sleep(5)

    async def _monitor_trades(self):
        """Monitor trades for thresholds"""
        trade = self.risk_mgmt.trade
        broker = self.broker
        loss_limit = -abs(trade.loss.limit)
        open_positions = await self.broker.get_positions()
        for pos in open_positions:
            # Alpaca logic
            if type(broker) is Alpaca:
                if pos.unrealized_intraday_plpc < loss_limit:
                    action = trade.loss.action
                    print("Do action")
        


    async def _(self):
        """
        """
