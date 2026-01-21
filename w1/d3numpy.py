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
import sys
# listarray=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(listarray)
# print(listarray.dtype)
# print(listarray.shape)
# print(listarray.size)

# x=np.array({34,23},dtype=object)
# print(x,x.dtype)
# print(x.dtype)

# y=np.zeros((5,5))
# print(y)
# rng=np.arange(5)
# print(rng)
# lspace=np.linspace(1,50,120)
# print(lspace)
# emp=np.empty((4,6))
# print(emp)
# emp_like=np.empty_like(lspace)
# print(emp_like)
# ide = np.identity(54)
# print(ide.shape)
# print(ide)
arr=np.arange(10)
# print(arr.reshape(6,10))
arr=arr.reshape(5,2)
# arr=arr.ravel()
# print(arr)
# print(arr.sum(axis=1))
# print(arr.sum(axis=0))
# arr=arr.T
# arr=arr.flat
# print(arr)
# for item in arr.flat:
#     print(item)
# print(arr.shape)
# print(arr.ndim)
# print(arr.size)
# print(arr.nbytes)
# oneD=np.array([1,200,3,4,5])
# print(oneD.argmax())
# print(oneD.argmin())
# print(oneD.argsort())
# print(arr.argmax(axis=0))
# print(arr.argmax(axis=1))
# print(arr)
# print(arr.argsort(axis=0))
x=arr.ravel()
x=x.reshape(2,5)
# print(x)

x2=x

x3=x*x
# print(x3,np.sqrt(x3))
# print(np.where(x3>40))



py_arr=[0,3,423,23]
# np_arr=[2,3,4,2,4,2]
np_arr=np.array(py_arr)
np_arr=np.array(np_arr,np.int32)

print(sys.getsizeof(1)*len(py_arr))
print(np.size(np_arr)* np_arr.itemsize)