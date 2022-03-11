import pandas as pd
#import matplotlib.pyplot as plt
import numpy as np

#df = pd.read_csv('data.csv')
#print(df.info())

#df = pd.read_csv('dirtydata.csv')
#new_df = df.dropna()
#print(new_df.to_string())

#df = pd.read_csv('data1.csv')
#print(df.corr())
#df.plot( kind = 'scatter', x= 'Duration', y = 'Calories')
#plt.show()
#print(df.to_string())
#
#x = df["Calories"].mean()
#df["Calories"].fillna(x, inplace = True)
#df.fillna(130, inplace=True)
#df.dropna(inplace = True)
#print(df.to_string())
#x = "2020/12/22 "

#df["Date"] = pd.to_datetime(df['Date'])
#df.dropna(subset = ['Date'], inplace = True)
#df.loc[7, 'Duration'] = 45
#print(df.to_string())
#for x in df.index:
#    if df.loc[x, "Duration"] > 120:
#        df.loc[x, "Duration"] =120

#for x in df.index:
#    if df.loc[x, "Duration"] > 120:
#        df.drop(x, inplace = True)
#print(df.to_string())
#print(df.to_string())
#print(df.duplicated())

#df.drop_duplicates(inplace = True)
#print(df.duplicated())

#df.corr()

#d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
#   'Lee','David','Gasper','Betina','Andres']),
#   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
#   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
#}

#df = pd.DataFrame(d)
#print(df)

#def adder(ele1,ele2):
#   return ele1+ele2

#df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
#df.pipe(adder,2)
#print(df.apply(np.mean))
s1 = pd.Series([28220804648, 16179776932, 21229909340, 16126522783, 14666227351, 11172062661, 9501221177, 13778234614, 13194846235])
s2 = pd.Series([2440.352295, 2455.935059, 2468.030273, 2423.001221, 2547.092041, 2597.084717, 2603.466553, 2688.278809, 2792.117188])
df = {'Volume': s1, 'close': s2}
d = pd.DataFrame(df)
d['divide'] = d['Volume']/d['close']
d.pop('divide')
print(d)











