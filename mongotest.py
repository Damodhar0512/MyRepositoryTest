import pymongo

client = pymongo.MongoClient("mongodb+srv://ndamoo:Newyear2022@ineuron-d.lhbnr.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d = {
    "name" : "Damodhar",
    "email" : "Damodhar@gmail.com" ,
    "surname" : "sree"
 }

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)