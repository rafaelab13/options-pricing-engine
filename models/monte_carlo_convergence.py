
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('../models')
from monte_carlo import monte_carlo_option

# Paramètres
S = 100
K = 100
T = 1
r = 0.05
sigma = 0.2

# Nombre de simulations croissant
simulations = [100, 500, 1000, 2000, 5000, 10000, 50000, 100000]

call_prices = [monte_carlo_option(S, K, T, r, sigma, 'call', n) for n in simulations]
put_prices = [monte_carlo_option(S, K, T, r, sigma, 'put', n) for n in simulations]

# Valeurs Black-Scholes de référence
bs_call = 10.4506
bs_put = 5.5735


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle('Monte Carlo Convergence', fontsize=14)

ax1.plot(simulations, call_prices, marker='o', color='blue', label='Monte Carlo')
ax1.axhline(y=bs_call, color='red', linestyle='--', label='Black-Scholes')
ax1.set_xscale('log')
ax1.set_title('Call price')
ax1.set_xlabel('Number of simulations')
ax1.set_ylabel('Price')
ax1.legend()

ax2.plot(simulations, put_prices, marker='o', color='green', label='Monte Carlo')
ax2.axhline(y=bs_put, color='red', linestyle='--', label='Black-Scholes')
ax2.set_xscale('log')
ax2.set_title('Put price')
ax2.set_xlabel('Number of simulations')
ax2.set_ylabel('Price')
ax2.legend()

plt.tight_layout()
plt.savefig('convergence_plot.png')
plt.show()