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



