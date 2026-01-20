# import numpy as np
# # import sklearn



# myarr=np.array([[2,4,90,89]],np.int32)
# print(myarr[0])
# print(type(myarr[0]))
# print(myarr.shape)
# print(myarr.dtype)
# myarr[0,2]=89
# print(myarr)









# conversion from other python strucutres

import numpy as np
# listarray=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(listarray)
# print(listarray.dtype)
# print(listarray.shape)
# print(listarray.size)

# x=np.array({34,23},dtype=object)
# print(x,x.dtype)
# print(x.dtype)

y=np.zeros((5,5))
# print(y)
rng=np.arange(5)
# print(rng)
lspace=np.linspace(1,50,120)
# print(lspace)
emp=np.empty((4,6))
# print(emp)
emp_like=np.empty_like(lspace)
# print(emp_like)
ide = np.identity(54)
# print(ide.shape)
# print(ide)
arr=np.arange(60)
print(arr.reshape(6,10))
arr=arr.reshape(6,10)
arr=arr.ravel()
print(arr)