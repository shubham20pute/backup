import pymongo
client1 = pymongo.MongoClient("mongodb+srv://priyanka:mam@cluster0.grmre.mongodb.net/test?retryWrites=true&w=majority")
client2 = pymongo.MongoClient("mongodb://localhost:27017")
db1 = client1.test
db2 = client2.test
crsr = db1.list_collections()
collectionList = []
for c in crsr:
    collectionList.append(c['name'])
print(collectionList)

for collectionName in collectionList:
    data = db1[collectionName].find({})
    dataList = []
    for d in data:
        dataList.append(d)
    print(f'_________________{collectionName}_________________')
    print(dataList)
    db2[collectionName].delete_many({})
    db2[collectionName].insert_many(dataList)