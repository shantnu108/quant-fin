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





















# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# intCap=100_000
# nPeriods=252
# mu=0.10
# sigma=0.20

# # np.random.seed(42)
# dailyMu=mu/252
# dailyVol=sigma/np.sqrt(252)

# returns = np.random.normal(loc=dailyMu,scale=dailyVol,size=nPeriods)
# # print(returns)
# wrongWealth = intCap * (1 + returns.sum())

# wealth=[intCap]
# for r in returns:
#     newWealth=wealth[-1] * (1+r)
#     wealth.append(newWealth)

# df = pd.DataFrame({
#     "Daily Return":returns,
#     "Wealth":wealth[1:]
# })
# df.head()


# plt.figure(figsize=(10,5))
# plt.plot(df["Wealth"])
# plt.axhline(intCap,linestyle="--")
# plt.title("Compounding wealth over time")
# plt.xlabel("days")
# plt.ylabel("Cap")
# plt.show()

# print("final wealth right ",round(df["Wealth"].iloc[-1],2))
# print("final wealth wrong",round(wrongWealth,2))




































































# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# intCap=100_000
# nPeriods=252
# mu=0.10
# sigma=0.20

# # np.random.seed(42)

# dailyMu=mu/252
# dailyVol=sigma/np.sqrt(nPeriods)

# returnsA=np.random.normal(dailyMu,dailyVol,nPeriods)
# returns2=np.random.normal(dailyMu,dailyVol,nPeriods)

# # returnsA=returns.copy()

# returnsB=np.random.permutation(returns2)

# def compundWealth(returns,startCap):
#     wealth=[startCap]
#     for r in returns:
#         wealth.append(wealth[-1]*(1+r))
#     return np.array(wealth[1:])

# wealthA=compundWealth(returnsA,intCap)
# wealthB=compundWealth(returnsB,intCap)


# df=pd.DataFrame({
#     "WealthA":wealthA,"WealthB":wealthB
# })

# print("final wealth a",round(df["WealthA"].iloc[-1],2))
# print("final wealth b",round(df["WealthB"].iloc[-1],2))


# def drawdown(wealth):
#     peak=np.maximum.accumulate(wealth)
#     dd=(wealth-peak)/peak
#     return dd

# ddA=drawdown(wealthA)
# ddB=drawdown(wealthB)

# print("Max Drawdown A:", round(ddA.min()*100, 2), "%")
# print("Max Drawdown B:", round(ddB.min()*100, 2), "%")

# plt.figure(figsize=(12,5))
# plt.plot(df["WealthA"],label="A")
# plt.plot(df["WealthB"],label="B")
# plt.axhline(intCap,linestyle="--")
# plt.legend()
# plt.title("same mean")
# plt.show()













