import pandas as pd
import numpy as np

ser=pd.Series((np.random.rand(34)*100).astype(int))
# print(ser)
print(type(ser))


df = pd.DataFrame(np.random.rand(334,5), index=np.arange(334))
# print(df.head())
# print(type(df))
# print(df.describe())
# print()
# print("Changing Column Names: ")
df.columns = list('ABCDE')
# print(df.head())

# df = df.drop('A', axis=1)
df = df.drop(0, axis=0)
print(df.head())
newdf = df.loc[(df['A']<0.8) & (df.loc(df['C']>0.1))]
print(newdf.head())