import pandas as pd 

df = pd.read_csv('./scooter.csv')
print(df.head(10))
print(df.columns)
print(df.dtypes)
print(df.loc[34221])
print(df.at[34221,'DURATION'])
print(df.where(df['user_id']==8417864))
print(df[(df['user_id'] == 8417864)])
one = df['user_id']==8417864
two = df['trip_ledger_id']==1488838
print(df.where( one & two))
print(df[(one) & (two)])
print(df.describe())
print(df.isnull().sum())