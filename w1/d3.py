import numpy as np

def runSimulation(samples):
    roll = np.random.randint(1,7,size=samples)
    samplemean = np.mean(roll)
    return samplemean


sampleSizes=[10,100,1000,10000]
print(f"{'Sample Size (N)':} | {'Sample Mean'} | {'Difference from 3.5'}")

for n in sampleSizes:
    mean=runSimulation(n)
    diff = abs(mean-3.5)

    print(f"{n:<15} | {mean:<15.4f} | {diff:<15.4f}")