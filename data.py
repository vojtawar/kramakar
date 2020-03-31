import pymongo as pm

def run():
    hostName = 'localhost'
    dbPort = 27017
    client = pm.MongoClient("mongodb://%s:%s" % (hostName, dbPort))
    db = client["database"]
    global users
    global things
    users = db["users"]
    things = db["things"]
    print("almost created")
    x = users.insert_one({"name": "borec", "email": "bruh@gmail.com"})
    print("inserted one dict, ", x.inserted_id)
    y = things.insert_one({"name": "sur1", "price": 21})
    print("inserted both dicts, ", y.inserted_id)
