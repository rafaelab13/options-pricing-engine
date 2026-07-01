

import numpy as np
def monte_carlo_option(S, K, T, r, sigma, option_type='call', n_simulations=10000):
    
    # Simuler les prix finaux
    Z = np.random.standard_normal(n_simulations)
    ST = S * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)
    
    # Calculer le payoff
    if option_type == 'call':
        payoffs = np.maximum(ST - K, 0)
    else:
        payoffs = np.maximum(K - ST, 0)
    
    # Actualiser
    price = np.exp(-r * T) * np.mean(payoffs)
    return price

