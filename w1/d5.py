# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt


# # np.random.seed(42)
# intCap=100_00_000

# returns=np.random.normal(0.07/252,0.01/np.sqrt(252),1000)
# print(returns)

# wealth=[intCap]

# for r in returns:
#     new_wealth=wealth[-1]*(1+r)
#     wealth.append(new_wealth)





# fig,ax=plt.subplots(figsize=(12,6))
# ax.plot(wealth,label="returns",color="red",linestyle="-",linewidth=2)
# ax.axhline(y=intCap, linestyle="--", linewidth=2, label="Initial Capital")
# ax.legend()
# ax.grid(False)
# plt.show()
# # print(x2)
# print(wealth[-1])





















import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

intCap=100_000
nPeriods=252
mu=0.10
sigma=0.20

# np.random.seed(42)
dailyMu=mu/252
dailtVol=sigma/np.sqrt(252)

returns = np.random.normal(loc=dailyMu,scale=dailtVol,size=nPeriods)
wealth=[intCap]
for r in returns:
    newWealth=wealth[-1] * (1+r)
    wealth.append(newWealth)

df = pd.DataFrame({
    "Daily Return":returns,
    "Wealth":wealth[1:]
})
df.head()


plt.figure(figsize=(10,5))
plt.plot(df["Wealth"])
plt.axhline(intCap,linestyle="--")
plt.title("Compounding wealth over time")
plt.xlabel("days")
plt.ylabel("Cap")
plt.show()