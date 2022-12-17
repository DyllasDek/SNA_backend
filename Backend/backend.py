from flask import Flask, request, abort, jsonify
from flask_cors import CORS
import os
import pymongo


client = pymongo.MongoClient('mongodb://pl:pl@mongo_db:27017/game')
db = client['game']['score']



app = Flask(__name__)
CORS(app)

def db_find(nick):
	for x in db.find({'CurrentName':f'{nick}'},{'_id':0, 'CurrentName': 1, 'CurrentScore': 1, 'CurrentMaxScore': 1}):
		return x
	
def db_update(nick,info):
	filter = { 'CurrentName': f'{nick}' }
	val = {"$set": info}
	db.update_one(filter,val)

@app.route('/getplayer', methods=['POST'])
def GetPlayer():
	if not request.data:
		abort(400)
	nick = request.data.decode('ascii')
	query = db_find(nick)
	if not query:
		resp = {'CurrentName':nick,'CurrentScore':0,'CurrentMaxScore':0}
		db.insert_one(resp)
		query = db_find(nick)
	return jsonify(query), 200

@app.route('/updatescore', methods=['POST'])
def UpdateScore():
	if not request.json :
		abort(400)
	data = request.json
	nick = data['CurrentName']
	del data['CurrentName']
	db_update(nick,data)
	return jsonify({'resp': True}), 200

@app.route('/gettop', methods=['GET'])
def GetTop():
    resp= [x for _,x in zip(range(5),db.find({},{'_id':0, 'CurrentName': 1, 'CurrentScore': 1, 'CurrentMaxScore': 1}).sort('CurrentMaxScore',-1))]
    return jsonify({'Top':resp}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 30000))
    app.run(host='0.0.0.0',debug=True, port = port)
