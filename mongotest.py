import pymongo
client = pymongo.MongoClient("mongodb://JakiPolad:jakipolad@ac-iuwekda-shard-00-00.blamz0a.mongodb.net:27017,ac-iuwekda-shard-00-01.blamz0a.mongodb.net:27017,ac-iuwekda-shard-00-02.blamz0a.mongodb.net:27017/?ssl=true&replicaSet=atlas-fqiikr-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name" : "Mohamadjaki",
    "email" : "jakipolad13@gmail.com",
    "surname"  : "Polad"
}

db1 = client["mongotest"]
coll = db1["test"]
coll.insert_one(d)