import numpy as np


# np.random.seed(50)
random_returns=np.random.normal(0,1,1000)
# # print(rand_returns)
# print(rand_returns[:5])



start_p=100000
volatility=0.02

price_path=[start_p]
for r in random_returns[:30]:
    nextPrice = price_path[-1] * (1+r*volatility)
    price_path.append(nextPrice)


print(f"Ending after 30 days{price_path[-1]:.2f}")

