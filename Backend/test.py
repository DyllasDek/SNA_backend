import pymongo
"mongodb+srv://user:pass@cluster.mongodb.net/myFirstDatabase"
client = pymongo.MongoClient('mongodb://pl:pl@localhost:27017/game')

db = client['game']

users = db['score']


#docs = [
#	{"CurrentName": "Danka", "CurrentScore": 0, "CurrentMaxScore": 10},
#	{"CurrentName": "Anka", "CurrentScore": 0, "CurrentMaxScore": 20},
#	{"CurrentName": "Yrka", "CurrentScore": 0, "CurrentMaxScore": 5},
#   ]
#users.insert_many(docs)

for x in users.find().sort('CurrentMaxScore',-1):
	print(x)
#print('pipy check')
#x = [x for _,x in zip(range(5),users.find({},{'_id':0, 'CurrentName': 1, 'CurrentScore': 1, 'CurrentMaxScore': 1}).sort('CurrentMaxScore',-1))]
#print(x)
#resp= [x for _,x in zip(range(5),db.find({},{'_id':0, 'CurrentName': 1, 'CurrentScore': 1, 'CurrentMaxScore': 1}).sort('CurrentMaxScore',-1))]
#print(resp)
