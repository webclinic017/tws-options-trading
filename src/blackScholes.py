# Implementing the Black-Scholes Formula in Python

import numpy as np
from scipy.stats import norm

# define variables
r = 0.01
S = 30
K = 40
T = 240 / 365
sigma = 0.3


def blackScholes(r, S, K, T, sigma, type="C"):
    """Calculate BS option price for a call/put

    Args:
        r (float): _description_
        S (_type_): _description_
        K (_type_): _description_
        T (_type_): _description_
        sigma (_type_): _description_
        type (str, optional): _description_. Defaults to "C".
    """

    d1 = (np.log(S / K) + (r + sigma**2 / 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    try:
        if type == "C":
            price = S * norm.cdf(d1, 0, 1) - K * np.exp(-r * T) * norm.cdf(d2, 0, 1)
        elif type == "P":
            price = K * np.exp(-r * T) * norm.cdf(-d2, 0, 1) - S * norm.cdf(-d1, 0, 1)
        return price

    except:
        print("Please confirm all option parameters above!")


print("Option Price is: ", round(blackScholes(r, S, K, T, sigma, type="C"), 2))
