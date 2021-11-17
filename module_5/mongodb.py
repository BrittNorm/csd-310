# Brittany Normandin, CSD 310, 11/17/2021
#Module 5 Assignment 5.2

from pymongo import MongoClient

uri="mongodb+srv://admin:admin@cluster0.9s1rm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string

client = MongoClient(uri,  tls=True, tlsAllowInvalidCertificates=True)

db = client.pytech

print(db.list_collection_names())
