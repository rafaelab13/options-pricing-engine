import numpy as np
from scipy.stats import norm
import sys
sys.path.append('../models')
from black_scholes import calculate_d1_d2

#Delta
def delta(S, K, T, r, sigma, option_type='call'):
    d1, d2 = calculate_d1_d2(S, K, T, r, sigma)
    if option_type == 'call':
        return norm.cdf(d1)
    else:
        return norm.cdf(d1) - 1   # for the put


#Gamma
def gamma(S, K, T, r, sigma):
    d1, d2 = calculate_d1_d2(S, K, T, r, sigma)
    return norm.pdf(d1) / (S * sigma * np.sqrt(T))


#Vega
def vega(S, K, T, r, sigma):
    d1, d2 = calculate_d1_d2(S, K, T, r, sigma)
    return S * norm.pdf(d1) * np.sqrt(T)

#Theta
def theta(S, K, T, r, sigma, option_type='call'):
    d1, d2 = calculate_d1_d2(S, K, T, r, sigma)
    if option_type == 'call':
        return (- (S * norm.pdf(d1) * sigma) / (2 * np.sqrt(T)) 
                - r * K * np.exp(-r * T) * norm.cdf(d2))
    else:
        return (- (S * norm.pdf(d1) * sigma) / (2 * np.sqrt(T)) 
                + r * K * np.exp(-r * T) * norm.cdf(-d2))
    
    
#Rho
def rho(S, K, T, r, sigma, option_type='call'):
    d1, d2 = calculate_d1_d2(S, K, T, r, sigma)
    if option_type == 'call':
        return K * T * np.exp(-r * T) * norm.cdf(d2)
    else:
        return -K * T * np.exp(-r * T) * norm.cdf(-d2)
    
    
# Test
S = 100
K = 100
T = 1
r = 0.05
sigma = 0.2

print(f"Delta call : {delta(S, K, T, r, sigma, 'call'):.4f}")
print(f"Delta put  : {delta(S, K, T, r, sigma, 'put'):.4f}")
print(f"Gamma      : {gamma(S, K, T, r, sigma):.4f}")
print(f"Vega       : {vega(S, K, T, r, sigma):.4f}")
print(f"Theta call : {theta(S, K, T, r, sigma, 'call'):.4f}")
print(f"Theta put  : {theta(S, K, T, r, sigma, 'put'):.4f}")
print(f"Rho call   : {rho(S, K, T, r, sigma, 'call'):.4f}")
print(f"Rho put    : {rho(S, K, T, r, sigma, 'put'):.4f}")
    
    
    
    
    
    
    
    