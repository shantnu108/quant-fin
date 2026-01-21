import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# np.random.seed(42)
Nyears=10
daysPerYear=252
nDays=Nyears*daysPerYear

intCap=100_000



mu=0.07

volA=0.05
volB=0.40

dt=1/daysPerYear

dailyReturnsA=np.random.normal(mu*dt,volA*np.sqrt(dt),nDays)
dailyReturnsB=np.random.normal(mu*dt,volB*np.sqrt(dt),nDays)

# print(dailyReturnsA)

WA=intCap*np.cumprod(1+dailyReturnsA)
WB=intCap*np.cumprod(1+dailyReturnsB)

# wealth_A = intCap * np.cumprod(1 + dailyReturnsA)
# wealth_B = intCap * np.cumprod(1 + dailyReturnsB)

final_A=WA[-1]
final_B=WB[-1]

cagrA=(final_A/intCap)**(1/Nyears)-1
cagrB=(final_B/intCap)**(1/Nyears)-1

drag_a=mu-cagrA
drag_b=mu-cagrB

print("-------------10 year simulation results")
print(f"Asset A (low var): ${final_A:.2f}    Realized CAGR:{cagrA:.2%}")
print(f"Asset B (low var): ${final_B:.2f}    Realized CAGR:{cagrB:.2%}")
print("--"*30)
print(f"Variancee Drag A:{drag_a:.4%}")
print(f"Variancee Drag B:{drag_b:.4%}")














# plt.figure(figsize=(12, 6))

# # Plotting Wealth Paths
# # Using the arrays WA and WB you created
# plt.plot(WA, label=f'Asset A (Low Vol: 5%)', color='blue', linewidth=2)
# plt.plot(WB, label=f'Asset B (High Vol: 40%)', color='red', linewidth=1.5, alpha=0.7)

# # Adding a reference line for Initial Capital
# plt.axhline(y=intCap, color='black', linestyle='--', label='Initial Capital', alpha=0.5)

# # Labels and Styling
# plt.title(f'Wealth Path Simulation ({Nyears} Years)\nSame Mean Return (7%), Different Volatility', fontsize=14)
# plt.xlabel('Trading Days')
# plt.ylabel('Portfolio Value ($)')
# plt.legend(loc='upper left')
# plt.grid(True, linestyle='--', alpha=0.5)

# # Optional: Format Y-axis to look like currency
# import matplotlib.ticker as ticker
# formatter = ticker.StrMethodFormatter('${x:,.0f}')
# plt.gca().yaxis.set_major_formatter(formatter)

# plt.tight_layout()
# plt.savefig('volatility_drag_chart.png') # Saving the file
# plt.show()































plt.figure(figsize=(24,12))

plt.plot(WA,label="assest a low vol 5%",color="green",linewidth=2)
plt.plot(WB,label="assest b low vol 40%",color="red",linewidth=2,alpha=0.8)
plt.axhline(y=intCap,color="black",linestyle="--",label="int cap",alpha=0.5)
plt.title(f"Wealth path sim {Nyears} Years",fontsize=12)
plt.xlabel("trading days")
plt.ylabel("prot val $")
plt.grid(False,linestyle="--",alpha=0.5)
plt.tight_layout()
plt.show()






