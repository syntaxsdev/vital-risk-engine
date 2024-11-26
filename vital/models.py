from pydantic import BaseModel


class Profile(BaseModel):
    name: str
    description: str = None
    enabled: bool = False

class HealthCheck(BaseModel):
    route: str
    poll_delay: int = 5
    missed_polls_restart: int = 5


class App(BaseModel):
    host: str
    stop: str = None
    pause: str = None
    start: str = None
    health_check: HealthCheck | None


class RMTradeLoss(BaseModel):
    limit: int
    action: str


class RMTradeProfits(BaseModel):
    limit: int
    action: str


class Trade(BaseModel):
    loss: RMTradeLoss | None = None
    profits: RMTradeProfits | None = None


class RiskManagement(BaseModel):
    enabled: bool = True
    trade: Trade
