import numpy as np
import math
# uniformnumbers=np.random.rand(100)
# print(uniformnumbers)
# print(f"\nMin:{uniformnumbers.min():.4f},Max:{uniformnumbers.max():.4f}")
# # print(np.random.rand(10))

# normalnumbers=np.random.randn(100)
# print(normalnumbers)
# print(f"\nMin:{normalnumbers.min():.4f},Max:{normalnumbers.max():.4f}")
# # print("-" * 40)


# number = np.random.randn(10000000)

# # 2. Set printing format for the array
# np.set_printoptions(precision=4, suppress=True)

# # 3. Print the array (it will show a summarized version)
# print("The Numbers:")
# print(number)
# total=np.sum(number)
# # print(f"{number:.4f}")
# print("^"*50)
# x=total/10000000
# print(x)

flat_data = np.random.uniform(40, 70, 100000)

number=np.random.randn(10)
print(number)
print(flat_data)
total=sum(flat_data)
print(total/100000)