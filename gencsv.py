from faker import Faker
import csv
import pandas as pd
import json

df1=pd.read_csv('/home/aaman/code/data.csv')
print(df1.head(2))
print("-------------------")
output = open('data.csv','w')
fake = Faker()
#create 1000 csv rows
header=['name','age','street','city','state','zip','lng','lat']
mywriter = csv.writer(output)
mywriter.writerow(header)
for r in range(1000):
    mywriter.writerow([fake.name(),fake.random_int(min=18,max=80,step=1),
    fake.street_address(),fake.city(),fake.state(),fake.zipcode(),fake.longitude(),fake.latitude()])
output.close()

#read csv into dictionary
with open('data.csv') as f:
    myreader = csv.DictReader(f)
    headers = next(myreader)
    for row in myreader:
        print(row['name'],",",row['city'])
#load csv into pandas dataframe
df = pd.read_csv('data.csv')
print(df.head(10))

#create json file of 1000 records using Faker
output2 = open('data.json','w')

alldata = {}
alldata['records'] = []
for x in range(1000):
    data = {"name":fake.name(), "age":fake.random_int(min=18, max=80, step=1),
    "street":fake.street_address(),
    "city":fake.city(),"state":fake.state(),
    "zip":fake.zipcode(),
    "lng":float(fake.longitude()),
    "lat":float(fake.latitude())}
    alldata['records'].append(data)
json.dump(alldata,output2)
output2.close()

#read json file
with open("data.json", "r") as f2:
    data = json.load(f2)
    print(data['records'][0]['name'])
    for record in data['records']:
        print(record['name'],",",record['zip'])

#read json file into pandas df
df = pd.read_json('data.json')
print(df.head(10))

df2 = pd.json_normalize(df["records"])
print(df2.head(10))
print("Column orientation")
print(df2.head(1).to_json())
print('Record orientation')
print(df2.head(1).to_json(orient='records'))
