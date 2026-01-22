# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt


# # np.random.seed(42)
# Nyears=10
# daysPerYear=252
# nDays=Nyears*daysPerYear

# intCap=100_000



# mu=0.07

# volA=0.05
# volB=0.40

# dt=1/daysPerYear

# dailyReturnsA=np.random.normal(mu*dt,volA*np.sqrt(dt),nDays)
# dailyReturnsB=np.random.normal(mu*dt,volB*np.sqrt(dt),nDays)

# # print(dailyReturnsA)

# WA=intCap*np.cumprod(1+dailyReturnsA)
# WB=intCap*np.cumprod(1+dailyReturnsB)

# # wealth_A = intCap * np.cumprod(1 + dailyReturnsA)
# # wealth_B = intCap * np.cumprod(1 + dailyReturnsB)

# final_A=WA[-1]
# final_B=WB[-1]

# cagrA=(final_A/intCap)**(1/Nyears)-1
# cagrB=(final_B/intCap)**(1/Nyears)-1

# drag_a=mu-cagrA
# drag_b=mu-cagrB

# print("-------------10 year simulation results")
# print(f"Asset A (low var): ${final_A:.2f}    Realized CAGR:{cagrA:.2%}")
# print(f"Asset B (low var): ${final_B:.2f}    Realized CAGR:{cagrB:.2%}")
# print("--"*30)
# print(f"Variancee Drag A:{drag_a:.4%}")
# print(f"Variancee Drag B:{drag_b:.4%}")











# plt.figure(figsize=(24,12))

# plt.plot(WA,label="assest a low vol 5%",color="green",linewidth=2)
# plt.plot(WB,label="assest b low vol 40%",color="red",linewidth=2,alpha=0.8)
# plt.axhline(y=intCap,color="black",linestyle="--",label="int cap",alpha=0.5)
# plt.title(f"Wealth path sim {Nyears} Years",fontsize=12)
# plt.xlabel("trading days")
# plt.ylabel("prot val $")
# plt.grid(False,linestyle="--",alpha=0.5)
# plt.tight_layout()
# plt.show()































# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# def simulate_path(rets,start_val,withdrawl=0):
#     wealth=[start_val]
#     for r in rets:
#         curr_val=wealth[-1]*(1+r)
#         curr_val=curr_val-withdrawl
#         if curr_val<0:
#             curr_val=0
#         wealth.append(curr_val)
#     return wealth



# # np.random.seed(20)
# intWel=100_000
# yr=20

# mu=0.07
# vol=0.15
# randReturn=np.random.normal(mu,vol,yr)

# return_lucky=np.sort(randReturn)[::-1]

# return_unlucky=np.sort(randReturn)

# wealth_lucky_lump=simulate_path(return_lucky,intWel,withdrawl=0)
# wealth_unlucky_lump=simulate_path(return_unlucky,intWel,withdrawl=0)

# yearlyWithdrawl=5000

# wealth_lucky_lumpWD=simulate_path(return_lucky,intWel,withdrawl=yearlyWithdrawl)
# wealth_unlucky_lumpWD=simulate_path(return_unlucky,intWel,withdrawl=yearlyWithdrawl)

# fig, ax=plt.subplots(figsize=(14,6))
# ax.plot(wealth_lucky_lump,label="lucky path",color="green",linewidth=2)
# ax.plot(wealth_unlucky_lump,label="Unlucy path",color="red",linestyle="--",linewidth=2)

# ax.set_title(f"Lump Sum: Final Value is Identical\n(₹{int(wealth_lucky_lump[-1])} vs ₹{int(wealth_unlucky_lump[-1])})")

# ax.legend()
# ax.grid(True,alpha=0.3)
# plt.show()

# fig,ax1=plt.subplots(figsize=(12,6))
# ax1.plot(wealth_lucky_lumpWD,label="wealth lucky withdrawl",color="green",linewidth=2)
# ax1.plot(wealth_unlucky_lumpWD,label="wealth unlucky withdrawl",color="black",linestyle="--",linewidth=2)

# ax1.legend()
# ax1.grid(True,alpha=1)
# plt.show()







































import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

returns=np.random.normal(0,0.01,1000)

vol = np.zeros(1000)
vol[0]=0.01
for t in range(1,1000):
    vol[t]=0.1 * abs(returns[t-1])+0.9*vol[t-1]
    # print(abs(returns[t-1]))


clusteredReturns=vol*np.random.normal(0,1,1000)

plt.figure(figsize=(12,6))
plt.plot(clusteredReturns,label="clusered return",color="red",linewidth="0.3")
plt.grid(True,alpha=0.5)
plt.show()



