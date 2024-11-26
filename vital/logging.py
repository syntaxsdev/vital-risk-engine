import structlog
from logging import Logger

structlog.configure(
    processors=[
        structlog.processors.TimeStamper("iso"),
        structlog.processors.add_log_level,
        structlog.processors.format_exc_info,
        structlog.processors.JSONRenderer(),
    ]
)

logger: Logger = structlog.get_logger()