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

#get frequency counts of unique items of a series
ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))
print(ser)
uniq = ser.unique()
print(uniq)
print(ser.value_counts())

#keep only 2 most frequent values
val = ser.value_counts()
ser[~ser.isin(ser.value_counts().index[:2])] = 'Other'
print(ser.value_counts())
#split series into deciles
ser2 = pd.Series(np.random.random(20))

print(pd.qcut(ser2,q=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1],
labels=['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th']))

#reshape series into dataframe
ser3 = pd.Series(np.random.randint(1,10,35))
df3 = pd.DataFrame(ser3.values.reshape(7,5))
print(df3)

#find positions of numbers that are multiples of 3
ser4 = pd.Series(np.random.randint(1,10,7))
#print(np.argwhere(ser4 % 3))
mylist = list('abcdefghijklmnopqrstuvwxyz')
pSeries1 = pd.Series(mylist)
pos = [0,4,8,14,20]

for idx in pos:
    print(pSeries1[idx])

ser1 = pd.Series(range(5))
print(ser1)
ser2 = pd.Series(list('abcde'))
ser1.append(ser2)
print(ser1)
print(ser2)
df12 = pd.concat([ser1,ser2],axis = 1)
print(df12)

#get position of elements from another series
ser1 = pd.Series([10,9,6,5,3,1,12,8,13])
ser2 = pd.Series([1,3,10,13])
print([np.where(i == ser1)[0].tolist()[0] for i in ser2])
print([pd.Index(ser1).get_loc(el) for el in ser2])

#compute mean squared error
truth = pd.Series(range(10))
pred = pd.Series(range(10)) + np.random.random(10)
print("truth",truth)
print("pred",pred)
err = pow((pred - truth),2)
mse = 1/len(truth) * sum(err)
mse2 = np.mean(err)
print("err",err)
print("mse",mse)
print("mse2",mse2)

#convert elements
ser = pd.Series(['how','to','do','this'])
print(ser.map(lambda x: x.title()))
print(pd.Series([i.title() for i in ser]))