import pandas as pd 
import numpy as np 

#create pandas series
mylist = list('abcdefghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist,myarr))

pSeries1 = pd.Series(mylist)
print(pSeries1.head(5))
pSeries2 = pd.Series(myarr)
pSeries3 = pd.Series(mydict)
print(pSeries2.head(5))
print(pSeries3.head(5))

#convert the index of a series to a column of a dataframe
#This option is wrong
df1 = pd.DataFrame(pSeries3)
print(df1.head(5))
#This is correct
df2 = pSeries3.to_frame().reset_index()
print(df2.head())

#combine series to form a dataframe
pSeries1.name="alphabets"
df12 = pd.concat([pSeries1,pSeries2],axis=1)
print(df12)

ser1 = pd.Series([1,2,3,4,5])
ser2 = pd.Series([4,5,6,7,8])
ser3 = ser1[~ser1.isin(ser2)] #~ bitwise complement - thus returns all elements of ser1 not in ser2
ser4 = ser2[~ser2.isin(ser1)]
ser5 = ser1[ser1.isin(ser2)] #find values of ser1 also in ser2
print(ser3)
print(ser4)
print(ser5)

#get statistics of a series
ser4 = pd.Series(np.random.normal(10,5,25))
df4 = pd.DataFrame(ser4)
print(df4.describe())
print(np.percentile(ser4,q=[0,25,50,75,100]))
