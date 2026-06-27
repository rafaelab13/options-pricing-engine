# Options Pricing Engine 

A Python-based pricing engine for vanilla and exotic options, featuring three models, full Greeks analysis, and stress testing under different volatility regimes.

---

## Models implemented

- **Black-Scholes** : closed-form analytical solution for European options
- **Monte Carlo** : simulation-based pricing with convergence analysis
- **Binomial Tree** : Cox-Ross-Rubinstein model with tree visualization

## Greeks

Full sensitivity analysis : Delta, Gamma, Vega, Theta, Rho (computed analytically and visualized across spot prices).

## Exotic options

- Barrier options (knock-in / knock-out)
- Asian options (arithmetic average)

## Stress testing

Repricing under three volatility regimes : low vol (VIX < 15), normal, and high vol (VIX > 30) to simulate real market conditions.

---

## Project structure
options-pricing-engine/

├── models/          # Black-Scholes, Monte Carlo, Binomial Tree

├── greeks/          # Greeks computation and visualization

├── stress_testing/  # Vol regime stress tests

└── notebooks/       # Step-by-step walkthrough

## Tech stack

Python 3.12 · numpy · scipy · matplotlib · yfinance
