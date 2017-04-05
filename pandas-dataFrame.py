# -*- coding: utf-8 -*-
"""
Created on Wed Apr 05 20:18:39 2017

@author: kartkond
"""
import pandas as pd
def oddeven(num):
    if num%2==0:
        return num+5
    else:
        return num-5
    

col1 = [10,20,30,40]
for x in range(1,100):
    col1.append(x);
col2 = ['abc','def','xyz','pqr']
for x in range(1,100):
    col2.append((chr(x)))
col3 = [0,0,0,0]
for x in range(1,100):
    col3.append(0)
    
    
#creating data frame
df1 = pd.DataFrame({'col1':col1,
'col2':col2,'col3':col3})
df1.shape
df1.info()
df1.describe()
df1.head()
df1.head(2)
df1.tail()
df1['col4'] = 0
#access frame content by column/columns
df1.col1
df1['col2']
df1[['col2','col1']]
df1[[0,1]]

#dropping a column
df2 = df1.drop('col4',1)

#slicing rows of frame
df1[10:42]
df1[0:]
df1[:2]
df1[-2:]

#filtering rows of dataframe by condition
type(df1.col1 > 20)
df1[df1.col1>20]
df1[[0]].unique()
len(df1['col1'].unique())


#selecting subsets of rows and columns
df1.iloc[0:2,]
df1.iloc[[0,2],]
df1.iloc[0:2,0]
df1.iloc[0:2,[0,2]]
df1.loc[0:2,['col2']]

#grouping data in data frames
df1.groupby('col1').size()

df1['col1'].value_counts(dropna=False)
df1['col1'].apply(oddeven)