#operate on postgres through python psycopg2
import psycopg2 as db
from faker import Faker
import pandas as pd

conn_string = "dbname='dataengineering' host='localhost' user='postgres' password='postgres1'"
conn = db.connect(conn_string)
cur = conn.cursor()

df = pd.read_sql("select * from users",conn)
df.to_json(orient = 'records')
print(df.head(10))