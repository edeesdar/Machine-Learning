import numpy as np
import pandas as pd
# from io import StringIO,BytesIO 
# arr=np.arange(1,8)
# print(arr)
# df=pd.read_csv('project.csv')
# print(df.head)
# #fd=df['X0'].value_counts()
# #print(fd)
# fd=df[df['mark']>60]
# print(fd)
# data=('a,b,c\n'
#       '4,apple,5.6\n'
#       '8,orange,cow\n')
# gf=pd.read_csv(StringIO(data),index_col=False)
# print(gf)
# wine = pd.read_table("https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data",sep=",",header=None)
# print(wine.head())
# wine1=wine.to_json(orient='records')
# print(wine1)
df=pd.read_csv('seaborn/tips.csv')
print(df.head())