import numpy as np
import matplotlib.pyplot as plt
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

roll = np.random.randint(1,7,100000)
runningAvg=[]
for i in range(1,100001):
    slice=roll[:i]
    mean=np.mean(slice)
    runningAvg.append(mean)


plt.plot(runningAvg)

plt.axhline(y=3.5,color="y",linestyle="-",label="Targer avg of large no.")
plt.title("instablity to stability")
plt.xlabel("No of rolls")
plt.ylabel("Avg value")
plt.legend()
plt.show()