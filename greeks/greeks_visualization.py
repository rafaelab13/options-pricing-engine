import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('../models')
from black_scholes import calculate_d1_d2
from analytical_greeks import delta, gamma, vega, theta, rho

# Parameters
K = 100
T = 1
r = 0.05
sigma = 0.2

# Spot price from 60 to 140
S_range = np.linspace(60, 140, 200)

# Greeks for each price
deltas_call = [delta(S, K, T, r, sigma, 'call') for S in S_range]
deltas_put = [delta(S, K, T, r, sigma, 'put') for S in S_range]
gammas = [gamma(S, K, T, r, sigma) for S in S_range]
vegas = [vega(S, K, T, r, sigma) for S in S_range]
thetas_call = [theta(S, K, T, r, sigma, 'call') for S in S_range]
thetas_put = [theta(S, K, T, r, sigma, 'put') for S in S_range]
rhos_call = [rho(S, K, T, r, sigma, 'call') for S in S_range]
rhos_put = [rho(S, K, T, r, sigma, 'put') for S in S_range]

# Figure 1 — Call Greeks
fig1, axes1 = plt.subplots(2, 3, figsize=(14, 8))
fig1.suptitle('Call Greeks — Black-Scholes', fontsize=14)

axes1[0,0].plot(S_range, deltas_call, color='blue')
axes1[0,0].axvline(x=100, color='gray', linestyle='--', alpha=0.5)
axes1[0,0].set_title('Delta')

axes1[0,1].plot(S_range, gammas, color='green')
axes1[0,1].axvline(x=100, color='gray', linestyle='--', alpha=0.5)
axes1[0,1].set_title('Gamma')

axes1[0,2].plot(S_range, vegas, color='purple')
axes1[0,2].axvline(x=100, color='gray', linestyle='--', alpha=0.5)
axes1[0,2].set_title('Vega')

axes1[1,0].plot(S_range, thetas_call, color='orange')
axes1[1,0].axvline(x=100, color='gray', linestyle='--', alpha=0.5)
axes1[1,0].set_title('Theta')

axes1[1,1].plot(S_range, rhos_call, color='brown')
axes1[1,1].axvline(x=100, color='gray', linestyle='--', alpha=0.5)
axes1[1,1].set_title('Rho')

axes1[1,2].axis('off')
plt.tight_layout()
plt.savefig('call_greeks.png')
plt.show()

# Figure 2 — Put Greeks
fig2, axes2 = plt.subplots(2, 3, figsize=(14, 8))
fig2.suptitle('Put Greeks — Black-Scholes', fontsize=14)

axes2[0,0].plot(S_range, deltas_put, color='red')
axes2[0,0].axvline(x=100, color='gray', linestyle='--', alpha=0.5)
axes2[0,0].set_title('Delta')

axes2[0,1].plot(S_range, gammas, color='green')
axes2[0,1].axvline(x=100, color='gray', linestyle='--', alpha=0.5)
axes2[0,1].set_title('Gamma')

axes2[0,2].plot(S_range, vegas, color='purple')
axes2[0,2].axvline(x=100, color='gray', linestyle='--', alpha=0.5)
axes2[0,2].set_title('Vega')

axes2[1,0].plot(S_range, thetas_put, color='orange')
axes2[1,0].axvline(x=100, color='gray', linestyle='--', alpha=0.5)
axes2[1,0].set_title('Theta')

axes2[1,1].plot(S_range, rhos_put, color='brown')
axes2[1,1].axvline(x=100, color='gray', linestyle='--', alpha=0.5)
axes2[1,1].set_title('Rho')

axes2[1,2].axis('off')
plt.tight_layout()
plt.savefig('put_greeks.png')
plt.show()