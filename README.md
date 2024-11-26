# VITAL - Risk Management Engine
Volatility Intervention and Trade Analysis Layer (VITAL)

This can be added to trading algorithms to help wth logging, metrics, alerts, and other features. It can also be a standalone application that runs containerized or locally.

## Compatible Brokers
- [Alpaca](https://alpaca.markets/)

(More can be extended, please see [`vital/brokers`](https://github.com/syntaxsdev/vital-risk-engine/tree/main/vital/brokers))

## Features
- Trade alerts
- Logging
- Emergency liquidation
- Run and perform actions based on an algo health check
- Halting/pausing an algo
- Resuming an algo
- Monitors account
- Abnormality checks
    - overleveraged

## Future Potential Ideas
- Earnings report hedging/liquidation
- Inform an algo of important events upcoming by API route 