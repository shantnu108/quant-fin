import numpy as np
import pandas as pd
# np.random.seed(42)

trialCounts=[10,100,1000,10000,100000,1000000]


for n in trialCounts:
    tosses=np.random.randint(0,2,size=n)

    heads=np.sum(tosses)
    tails=n-heads

    probHead=heads/n

    error=abs(probHead-0.5)

    print(f"{n:<15}  | {heads:<10} | {tails:<10} | {probHead:.4f} ({probHead*100:5.2f}%) | {error:.4f}")