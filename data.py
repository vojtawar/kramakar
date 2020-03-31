import pymongo as pm

client = pm.MongoClient("mongodb://%s:%s" % (hostName, serverPort))
db = client["database"]
users = db["users"]
things = db["things"]
