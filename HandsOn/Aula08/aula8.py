from pymongo import MongoClient

client = MongoClient('127.0.0.1')
db = client['devops']

#db.fila.insert({
#	"servico": "intranet",
#	"status":0

#})

#db.fila.insert({
#	"_id": 3,
#	"servico": "dns",
#	"status":0

#})

#UPDATE 

db.fila.update({
	"_id": 3, "servico": "dns"},
	{"$set": {"status":1}

})
#DELETE 
db.fila.remove({"_id": 3})

for d in db.fila.find({}):
	print d

