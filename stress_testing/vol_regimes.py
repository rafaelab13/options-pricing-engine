import numpy as np
import matplotlib.pyplot as plt
import sys
if '../models' not in sys.path:
    sys.path.append('../models')
if '../greeks' not in sys.path:
    sys.path.append('../greeks')
from black_scholes import black_scholes_call, black_scholes_put
from analytical_greeks import delta, gamma, vega, theta, rho

# Volatility regimes
regimes = {
    'Low vol (VIX < 15)'    : 0.10,
    'Normal vol (VIX 15-25)': 0.20,
    'High vol (VIX > 30)'   : 0.40
}

# Base parameters
S = 100
K = 100
T = 1
r = 0.05

# Calculate prices and Greeks for each regime
results = {}

for regime, sigma in regimes.items():
    results[regime] = {
        'sigma'      : sigma,
        'call_price' : black_scholes_call(S, K, T, r, sigma),
        'put_price'  : black_scholes_put(S, K, T, r, sigma),
        'delta_call' : delta(S, K, T, r, sigma, 'call'),
        'delta_put'  : delta(S, K, T, r, sigma, 'put'),
        'gamma'      : gamma(S, K, T, r, sigma),
        'vega'       : vega(S, K, T, r, sigma),
        'theta_call' : theta(S, K, T, r, sigma, 'call'),
        'rho_call'   : rho(S, K, T, r, sigma, 'call')
    }
   # Print results table
print(f"{'Regime':<25} {'Call':>8} {'Put':>8} {'Delta':>8} {'Gamma':>8} {'Vega':>8} {'Theta':>8}")
print("-" * 75)

for regime, vals in results.items():
    print(f"{regime:<25} {vals['call_price']:>8.4f} {vals['put_price']:>8.4f} {vals['delta_call']:>8.4f} {vals['gamma']:>8.4f} {vals['vega']:>8.4f} {vals['theta_call']:>8.4f}") 
    
   
  # Visualization
labels = list(regimes.keys())
call_prices = [results[r]['call_price'] for r in labels]
put_prices = [results[r]['put_price'] for r in labels]
deltas = [results[r]['delta_call'] for r in labels]
gammas = [results[r]['gamma'] for r in labels]
vegas = [results[r]['vega'] for r in labels]
thetas = [results[r]['theta_call'] for r in labels]

fig, axes = plt.subplots(2, 3, figsize=(14, 8))
fig.suptitle('Stress Testing — Volatility Regimes', fontsize=14)

colors = ['green', 'orange', 'red']

axes[0,0].bar(labels, call_prices, color=colors)
axes[0,0].set_title('Call price')
axes[0,0].tick_params(axis='x', rotation=15)

axes[0,1].bar(labels, put_prices, color=colors)
axes[0,1].set_title('Put price')
axes[0,1].tick_params(axis='x', rotation=15)

axes[0,2].bar(labels, deltas, color=colors)
axes[0,2].set_title('Delta (call)')
axes[0,2].tick_params(axis='x', rotation=15)

axes[1,0].bar(labels, gammas, color=colors)
axes[1,0].set_title('Gamma')
axes[1,0].tick_params(axis='x', rotation=15)

axes[1,1].bar(labels, vegas, color=colors)
axes[1,1].set_title('Vega')
axes[1,1].tick_params(axis='x', rotation=15)

axes[1,2].bar(labels, thetas, color=colors)
axes[1,2].set_title('Theta (call)')
axes[1,2].tick_params(axis='x', rotation=15)

plt.tight_layout()
plt.savefig('stress_test_plot.png')
plt.show()  
   
    
   
    
   
    
   
    
   
    
   
    
