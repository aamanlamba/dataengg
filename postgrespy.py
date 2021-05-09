#operate on postgres through python psycopg2
import psycopg2 as db
from faker import Faker

conn_string = "dbname='dataengineering' host='localhost' user='postgres' password='postgres1'"
conn = db.connect(conn_string)
cur = conn.cursor()
fake = Faker()


#query = "insert into users (id,name, street, city, zip) values ({},'{}','{}','{}','{}')".format(1,'Big Bird','Sesame St','Fakeville','12345')
#print(cur.mogrify(query))

#query2 = "insert into users (id,name,street, city, zip) values (%s,%s,%s,%s,%s)"
#data = (1,'Big Bird','Sesame St','Fakeville','12345')
#generate 1000 records
data = []
maxID = "select max(id) from users"
cur.execute(maxID)
for rec in cur:
    i = int(rec[0])+1
print("ID: ",i)

for r in range(1000):
    data.append((i,fake.name(),fake.street_address(),
    fake.city(),fake.zipcode()))
    i+=1
#convert to array of tuples
data_for_db = tuple(data)
query2 = "insert into users (id,name,street, city, zip) values (%s,%s,%s,%s,%s)"


print(cur.mogrify(query2,data_for_db[1]))

cur.executemany(query2,data_for_db)
conn.commit()

#fetch data from db
query3 = "select * from users"
cur.execute(query3)

f = open('./fromdb.csv','w')
cur.copy_to(f,'users',sep=',')
f.close()

