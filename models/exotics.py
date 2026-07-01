import numpy as np
def barrier_option(S, K, T, r, sigma, barrier, option_type='call', barrier_type='knock-out', n_simulations=10000, n_steps=252):
    
    dt = T / n_steps
    payoffs = []
    
    for _ in range(n_simulations):
        # Simulate a full price path
        prices = [S]
        for _ in range(n_steps):
            Z = np.random.standard_normal()
            prices.append(prices[-1] * np.exp((r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z))
        
        # Check if barrier is hit
        touched = any(p >= barrier for p in prices)
        
        # Calculate payoff
        ST = prices[-1]
        if barrier_type == 'knock-out':
            if touched:
                payoffs.append(0)
            else:
                if option_type == 'call':
                    payoffs.append(max(ST - K, 0))
                else:
                    payoffs.append(max(K - ST, 0))
    
    return np.exp(-r * T) * np.mean(payoffs)


def asian_option(S, K, T, r, sigma, option_type='call', n_simulations=10000, n_steps=252):
    
    dt = T / n_steps
    payoffs = []
    
    for _ in range(n_simulations):
        # Simulate a full price path
        prices = [S]
        for _ in range(n_steps):
            Z = np.random.standard_normal()
            prices.append(prices[-1] * np.exp((r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z))
        
        # Payoff based on average price
        avg_price = np.mean(prices)
        
        if option_type == 'call':
            payoffs.append(max(avg_price - K, 0))
        else:
            payoffs.append(max(K - avg_price, 0))
    
    return np.exp(-r * T) * np.mean(payoffs)








# Test
S = 100
K = 100
T = 1
r = 0.05
sigma = 0.2
barrier = 120

barrier_call = barrier_option(S, K, T, r, sigma, barrier, 'call', 'knock-out')
asian_call = asian_option(S, K, T, r, sigma, 'call')

print(f"Barrier knock-out call : {barrier_call:.4f}")
print(f"Asian call             : {asian_call:.4f}")
print(f"Vanilla call (BS)      : 10.4506")







