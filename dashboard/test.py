from pymongo import MongoClient

client = MongoClient('localhost', 27017)
print(client.list_database_names())
db = client['fucking-db']
mycol = db["fuckyou"]

x = mycol.insert_one({"name":"merong"})

print(db.list_collection_names())

for wow in mycol.find():
    print(wow)

