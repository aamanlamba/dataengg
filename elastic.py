#use elasticsearch as a nosql backend
from elasticsearch import Elasticsearch, helpers
from faker import Faker
fake = Faker()

es = Elasticsearch()
doc = {"name": fake.name(),"street":fake.street_address(),
"city": fake.city(), "zip":fake.zipcode()}
res = es.index(index="users",doc_type="doc",body=doc)
print(res['result'])

actions = [
    {
        "_index":"users",
        "_type": "doc",
        "_source":{
            "name":fake.name(),
            "street":fake.street_address(),
            "city": fake.city(),
            "zip": fake.zipcode()
        }
    }
    for x in range(998)

]
res = helpers.bulk(es,actions)
print(res['result'])