import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'models'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'greeks'))

from black_scholes import black_scholes_call, black_scholes_put
from monte_carlo import monte_carlo_option
from binomial_tree import binomial_tree
from analytical_greeks import delta, gamma, vega, theta, rho

# Title
st.title("Options Pricing Engine")
st.markdown("Interactive pricing tool — Black-Scholes, Monte Carlo, Binomial Tree")

# Sidebar — parameters
st.sidebar.header("Parameters")

option_type = st.sidebar.radio("Option type", ["Call", "Put"])

S = st.sidebar.slider("Spot price (S)", 50, 200, 100)
K = st.sidebar.slider("Strike price (K)", 50, 200, 100)
T = st.sidebar.slider("Time to maturity (T) in years", 0.1, 3.0, 1.0)
r = st.sidebar.slider("Risk-free rate (r)", 0.0, 0.1, 0.05)
sigma = st.sidebar.slider("Volatility (σ)", 0.05, 0.8, 0.2)

# Pricing
opt = option_type.lower()

bs_price = black_scholes_call(S, K, T, r, sigma) if opt == 'call' else black_scholes_put(S, K, T, r, sigma)
mc_price = monte_carlo_option(S, K, T, r, sigma, opt)
bt_price = binomial_tree(S, K, T, r, sigma, option_type=opt)

# Display prices
st.subheader("Model prices")
col1, col2, col3 = st.columns(3)
col1.metric("Black-Scholes", f"${bs_price:.4f}")
col2.metric("Monte Carlo", f"${mc_price:.4f}")
col3.metric("Binomial Tree", f"${bt_price:.4f}")

# Greeks
st.subheader("Greeks")

d = delta(S, K, T, r, sigma, opt)
g = gamma(S, K, T, r, sigma)
v = vega(S, K, T, r, sigma)
t = theta(S, K, T, r, sigma, opt)
rh = rho(S, K, T, r, sigma, opt)

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Delta", f"{d:.4f}")
col2.metric("Gamma", f"{g:.4f}")
col3.metric("Vega", f"{v:.4f}")
col4.metric("Theta", f"{t:.4f}")
col5.metric("Rho", f"{rh:.4f}")

# Greeks chart
st.subheader("Greeks across spot prices")

S_range = np.linspace(60, 140, 200)
deltas = [delta(s, K, T, r, sigma, opt) for s in S_range]
gammas = [gamma(s, K, T, r, sigma) for s in S_range]
vegas = [vega(s, K, T, r, sigma) for s in S_range]
thetas = [theta(s, K, T, r, sigma, opt) for s in S_range]

fig, axes = plt.subplots(2, 2, figsize=(10, 6))

axes[0,0].plot(S_range, deltas, color='blue')
axes[0,0].axvline(x=S, color='gray', linestyle='--', alpha=0.5)
axes[0,0].set_title('Delta')

axes[0,1].plot(S_range, gammas, color='green')
axes[0,1].axvline(x=S, color='gray', linestyle='--', alpha=0.5)
axes[0,1].set_title('Gamma')

axes[1,0].plot(S_range, vegas, color='purple')
axes[1,0].axvline(x=S, color='gray', linestyle='--', alpha=0.5)
axes[1,0].set_title('Vega')

axes[1,1].plot(S_range, thetas, color='orange')
axes[1,1].axvline(x=S, color='gray', linestyle='--', alpha=0.5)
axes[1,1].set_title('Theta')

plt.tight_layout()
st.pyplot(fig)

# Stress testing
st.subheader("Stress Testing — Volatility Regimes")

regimes = {
    'Low vol (VIX < 15)': 0.10,
    'Normal vol (VIX 15-25)': 0.20,
    'High vol (VIX > 30)': 0.40
}

results = {}
for regime, sig in regimes.items():
    results[regime] = {
        'call_price': black_scholes_call(S, K, T, r, sig),
        'put_price': black_scholes_put(S, K, T, r, sig),
        'delta': delta(S, K, T, r, sig, opt),
        'gamma': gamma(S, K, T, r, sig),
        'vega': vega(S, K, T, r, sig),
        'theta': theta(S, K, T, r, sig, opt)
    }

df = pd.DataFrame(results).T
df.index.name = 'Regime'
st.dataframe(df.style.format("{:.4f}"))
