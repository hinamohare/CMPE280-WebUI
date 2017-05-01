import pymongo

dbconnection = pymongo.MongoClient()
dbname = dbconnection.cmpe280
collection = dbname.user

doc = collection.find_one()
name = doc["user"]
id = doc["_id"]

print name, id