import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# np.random.seed(42)
intCap=100_00_000

returns=np.random.normal(0.07/252,0.01/np.sqrt(252),1000)
print(returns)

wealth=[intCap]

for r in returns:
    new_wealth=wealth[-1]*(1+r)
    wealth.append(new_wealth)





fig,ax=plt.subplots(figsize=(12,6))
ax.plot(wealth,label="returns",color="red",linestyle="-",linewidth=2)
ax.axhline(y=intCap, linestyle="--", linewidth=2, label="Initial Capital")
ax.legend()
ax.grid(False)
plt.show()
# print(x2)
print(wealth[-1])