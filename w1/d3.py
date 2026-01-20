# import numpy as np
# import matplotlib.pyplot as plt
# def runSimulation(samples):
#     roll = np.random.randint(1,7,size=samples)
#     samplemean = np.mean(roll)
#     return samplemean


# sampleSizes=[10,100,1000,10000]
# print(f"{'Sample Size (N)':} | {'Sample Mean'} | {'Difference from 3.5'}")

# for n in sampleSizes:
#     mean=runSimulation(n)
#     diff = abs(mean-3.5)
#     print(f"{n:<15} | {mean:<15.4f} | {diff:<15.4f}")

# roll = np.random.randint(1,7,100000)
# runningAvg=[]
# for i in range(1,100001):
#     slice=roll[:i]
#     mean=np.mean(slice)
#     runningAvg.append(mean)


# plt.plot(runningAvg)

# plt.axhline(y=3.5,color="y",linestyle="-",label="Targer avg of large no.")
# plt.title("instablity to stability")
# plt.xlabel("No of rolls")
# plt.ylabel("Avg value")
# plt.legend()
# plt.show()




































































# import yfinance as yf
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np


# ticker = "RELAINCE.NS"
# data = yf.download(ticker,period="1y",progress=False)
# df = data[['Close']].copy()

# meanP=df["Close"].mean()
# df["returns"]=df["Close"].pctChange()
# meanR=df["returns"].mean()
# print(f"Stats for {ticker}")
# print(f"MeanP": {meanP:.2f})
# print()









































# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# np.random.seed(42)
# days=100

# priceChanges=np.random.normal(loc=1.001,scale=0.02,size=days)
# prices = 100*np.cumprod(priceChanges)

# df= pd.DataFrame(prices,columns=["Close_Price"])

# meanPrice=df["Close_Price"].mean()
# df["Returns"]=df["Close_Price"].pct_change()#(today - yesterday) / yesterday
# meanReturn=df["Returns"].mean()
# print(f"Mean Price{meanPrice:.2f}")

# fig,(ax1,ax2)=plt.subplots(2,1,figsize=(10,8),sharex=True)
# ax1.plot(df["Close_Price"])
# ax1.axhline(meanPrice,linestyle="--")
# ax2.plot(df["Returns"])
# plt.tight_layout()
# plt.show()


























import numpy as np

import matplotlib.pyplot as plt

TRUEmean=0.0005
STDdev=0.02
NUMdays=100000

dailyReturns=np.random.normal(loc=TRUEmean,scale=STDdev,size=NUMdays)
cumulativeSum=np.cumsum(dailyReturns)
daysCount=np.arange(1,NUMdays+1)
runningMean=cumulativeSum/daysCount
plt.figure(figsize=(12,6))
plt.plot(runningMean,color="red",linewidth=1.5,label="calulated runningmean")
plt.axhline(y=TRUEmean,color="green",linestyle="--",linewidth=1,label="True Mean")

plt.title('Convergence of Mean Return: Early Jumps vs Long-Run Settle')
plt.xlabel('Number of Days (Repetitions)')
plt.ylabel('Average Return')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()