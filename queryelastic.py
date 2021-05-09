from elasticsearch import Elasticsearch
from pandas.io.json import json_normalize

es = Elasticsearch()

doc = {"query":{"match_all":{}}}

res = es.search(index="users",body=doc,size=10)

for doc in res['hits']['hits']:
    print(doc['_source'])
df = json_normalize(res['hits']['hits'])
print(df.head(10))

res = es.search(index="users",q="name:Brianna Stewart",size=10)
for doc in res['hits']['hits']:
    print(doc['_source'])
