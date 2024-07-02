import pymongo
from pymongo import MongoClient

#mongo_client = MongoClient('mongodb://Qg4vMo9Slf0wa5DEd18b26VUcJ3X7sLT@tst1-shard-00-00-icprt.mongodb.net:27017')
mongo_client = MongoClient('mongodb://nexxis-boservices-dev01:Qg4vMo9Slf0wa5DEd18b26VUcJ3X7sLT@tst1-shard-00-00-icprt.mongodb.net:27017,tst1-shard-00-01-icprt.mongodb.net:27017,tst1-shard-00-02-icprt.mongodb.net:27017/nexxis-boservices-dev01?replicaSet=tst1-shard-0&ssl=true&authSource=admin')
#mongo_client = MongoClient('mongodb://localhost:27017/')
print("Connection Successful")

'''
list_of_db = mongo_client.list_database_names()
print(list_of_db)
db_name = 'mongo_test'
if db_name in list_of_db:
    print("DB:{} Exists !!".format(db_name))
else:
    # Creating a database name GFG
    db = mongo_client['mongo_test']
    print("Database is created !!")
'''

#Getting the database instance
db = mongo_client['nexxis-boservices-dev01']
#Creating a collection
collection = db['nexxis_test']

'''
try:
    db.validate_collection(collection)  # Try to validate a collection
    print('Collection already exist')
except pymongo.errors.OperationFailure as error:  # If the collection doesn't exist
    print(error)
    print("This collection doesn't exist")
    collection = db['nexxis_test2']
    print('Collection Created')
'''

# Create a list of documents to be inserted
docs = [
    {"name": "John Doe", "age": 30, "city": "New York"},
    {"name": "Jane Smith", "age": 25, "city": "London"},
    {"name": "David Johnson", "age": 35, "city": "Paris"}
]

result = collection.insert_many(docs)
# Print the inserted document IDs
print("Inserted document IDs:", result.inserted_ids)
mongo_client.close()
