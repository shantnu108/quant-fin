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































import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def simulate_path(rets,start_val,withdrawl=0):
    wealth=[start_val]
    for r in rets:
        curr_val=wealth[-1]*(1+r)
        curr_val=curr_val-withdrawl
        if curr_val<0:
            curr_val=0
        wealth.append(curr_val)
    return wealth



# np.random.seed(20)
intWel=100_000
yr=20

mu=0.07
vol=0.15
randReturn=np.random.normal(mu,vol,yr)

return_lucky=np.sort(randReturn)[::-1]

return_unlucky=np.sort(randReturn)

wealth_lucky_lump=simulate_path(return_lucky,intWel,withdrawl=0)
wealth_unlucky_lump=simulate_path(return_unlucky,intWel,withdrawl=0)

yearlyWithdrawl=5000

wealth_lucky_lumpWD=simulate_path(return_lucky,intWel,withdrawl=yearlyWithdrawl)
wealth_unlucky_lumpWD=simulate_path(return_unlucky,intWel,withdrawl=yearlyWithdrawl)

fig, ax=plt.subplots(figsize=(14,6))
ax.plot(wealth_lucky_lump,label="lucky path",color="green",linewidth=2)
ax.plot(wealth_unlucky_lump,label="Unlucy path",color="red",linestyle="--",linewidth=2)

ax.set_title(f"Lump Sum: Final Value is Identical\n(₹{int(wealth_lucky_lump[-1])} vs ₹{int(wealth_unlucky_lump[-1])})")

ax.legend()
ax.grid(True,alpha=0.3)
plt.show()

fig,ax1=plt.subplots(figsize=(12,6))
ax1.plot(wealth_lucky_lumpWD,label="wealth lucky withdrawl",color="green",linewidth=2)
ax1.plot(wealth_unlucky_lumpWD,label="wealth unlucky withdrawl",color="black",linestyle="--",linewidth=2)

ax1.legend()
ax1.grid(True,alpha=1)
plt.show()












































# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# # --------------------------
# # 1. Setup the "Quant God" Environment
# # --------------------------
# initial_wealth = 100000  # ₹1 Lakh
# years = 20
# mu = 0.07    # 7% expected return
# sigma = 0.15 # 15% volatility

# # Generate random returns
# np.random.seed(42)
# returns = np.random.normal(mu, sigma, years)

# # --------------------------
# # 2. Create Two Paths (Same Returns, Different Order)
# # --------------------------
# # Path 1: Lucky Start (Best returns first)
# returns_lucky = np.sort(returns)[::-1]

# # Path 2: Unlucky Start (Worst returns first)
# returns_unlucky = np.sort(returns)

# # --------------------------
# # 3. Simulation Logic
# # --------------------------
# def simulate_path(rets, start_val, withdrawal=0):
#     wealth = [start_val]
#     for r in rets:
#         # Market Impact
#         curr_val = wealth[-1] * (1 + r)
        
#         # Cashflow Impact (e.g., withdrawals)
#         curr_val -= withdrawal
        
#         # Bankruptcy check
#         if curr_val < 0:
#             curr_val = 0
        
#         wealth.append(curr_val)
#     return wealth

# # Case A: Pure Lump Sum (No Withdrawals)
# wealth_lucky_lump = simulate_path(returns_lucky, initial_wealth, withdrawal=0)
# wealth_unlucky_lump = simulate_path(returns_unlucky, initial_wealth, withdrawal=0)

# # Case B: Real Life (With Withdrawals - Sequence Risk)
# yearly_withdrawal = 8000
# wealth_lucky_wd = simulate_path(returns_lucky, initial_wealth, withdrawal=yearly_withdrawal)
# wealth_unlucky_wd = simulate_path(returns_unlucky, initial_wealth, withdrawal=yearly_withdrawal)

# # --------------------------
# # 4. Visualization
# # --------------------------
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# # Plot 1: Lump Sum (The Mathematical Truth)
# ax1.plot(wealth_lucky_lump, label='Lucky Path (High Returns First)', linewidth=2)
# ax1.plot(wealth_unlucky_lump, label='Unlucky Path (Losses First)', linestyle='--', linewidth=2)
# ax1.set_title(
#     f"Lump Sum: Final Value is Identical\n"
#     f"(₹{int(wealth_lucky_lump[-1])} vs ₹{int(wealth_unlucky_lump[-1])})"
# )
# ax1.legend()
# ax1.grid(True, alpha=0.3)

# # Plot 2: With Withdrawals (The Financial Reality)
# ax2.plot(wealth_lucky_wd, label='Lucky Path (High Returns First)', linewidth=2)
# ax2.plot(wealth_unlucky_wd, label='Unlucky Path (Losses First)', linestyle='--', linewidth=2)
# ax2.set_title("With Withdrawals: Path Kills You\n(Sequence of Returns Risk)")
# ax2.legend()
# ax2.grid(True, alpha=0.3)

# plt.show()

# # --------------------------
# # 5. Quick Stats
# # --------------------------
# print("--- QUANT REALITY CHECK ---")
# print(f"Lump Sum Diff: {wealth_lucky_lump[-1] - wealth_unlucky_lump[-1]:.2f} (Maths works!)")
# print(f"Withdrawal Scenario Diff: {wealth_lucky_wd[-1] - wealth_unlucky_wd[-1]:.2f} (Path Matters!)")



























