import numpy as np

days=252
intCap=100000
mu=0.0005
sigma=0.02
dailyReturns=np.random.normal(mu,sigma,days)

WealthPath=intCap*np.cumprod(1+dailyReturns)


realizedMean=np.mean(dailyReturns)
realizedStd=np.std(dailyReturns)

runningMax=np.maximum.accumulate(WealthPath)

drawdowns=(WealthPath-runningMax)/runningMax

maxDrawdown=np.min(drawdowns)

finalWealth=WealthPath[-1]

print("final wealth",finalWealth)
print(f"toal return{((finalWealth-intCap)/intCap)*100:.2f}%")
print(f"realized mean{realizedMean*100:.4f}%")
print(f"volatility{realizedStd*100:.4f}%")
print(f"worst dd {maxDrawdown*100:.2f}%")


if maxDrawdown < -0.50:
    print("survival status critical")
else:
    print("safe")