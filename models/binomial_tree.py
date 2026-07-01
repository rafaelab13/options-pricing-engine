import numpy as np
def binomial_tree(S, K, T, r, sigma, n_steps=100, option_type='call'):
    
    # Paramètres de l'arbre
    dt = T / n_steps
    u = np.exp(sigma * np.sqrt(dt))
    d = 1 / u
    p = (np.exp(r * dt) - d) / (u - d)
    
    # Prix finaux à l'expiration
    ST = np.array([S * (u**j) * (d**(n_steps-j)) for j in range(n_steps+1)])
    
    # Payoffs à l'expiration
    if option_type == 'call':
        payoffs = np.maximum(ST - K, 0)
    else:
        payoffs = np.maximum(K - ST, 0)
    
    # Remonter l'arbre
    for i in range(n_steps-1, -1, -1):
        payoffs = np.exp(-r * dt) * (p * payoffs[1:] + (1-p) * payoffs[:-1])
    
    return payoffs[0]



# Test
S = 100
K = 100
T = 1
r = 0.05
sigma = 0.2

bt_call = binomial_tree(S, K, T, r, sigma, option_type='call')
bt_put = binomial_tree(S, K, T, r, sigma, option_type='put')

print(f"Binomial Tree call : {bt_call:.4f}")
print(f"Binomial Tree put  : {bt_put:.4f}")
print(f"Black-Scholes call : 10.4506")
print(f"Black-Scholes put  : 5.5735")