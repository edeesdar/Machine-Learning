import numpy as np 
import pandas as pd
lst=[1,2,4,5,6]
arr=np.array(lst)
print(type(arr))
lst1=[2,4,5,6,6]
lst2=[3,4,56,6,7]
lst3=[4,6,8,9,8]
arr=np.array([lst1,lst2,lst3])
print(arr)
print(arr.shape)
arr=arr.reshape(1,15)
arr=np.arange(0,5)
print(arr)

df=pd.DataFrame(np.arange(0,20).reshape(5,4),[1,2,3,4,5],[1,2,3,4])
print(df)