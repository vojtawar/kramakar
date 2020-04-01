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
    print("db skeleton created")

    usersd = [
        {"name": "default", "email": "default@user.bruh", "passwd": "", "owns": {}, "buy": {}, "sell": {}}
    ]
    thingsd = [
        {"name": "sur1", "price": 4, "static": False, "buyable": True, "sellable": True},
        {"name": "money", "price": 1, "static": True, "buyable": False, "sellable": False},
        {"name": "sur2", "price": 2, "static": False, "buyable": True, "sellable": True},
        {"name": "points", "price": 0, "static": True, "buyable": False, "sellable": False},
        {"name": "fab1", "price": 10, "static": False, "buyable": True, "sellable": False},
        {"name": "fab2", "price": 20, "static": False, "buyable": True, "sellable": False}
    ]

    u = users.insert_many(usersd)
    print(u.inserted_ids)
    t = things.insert_many(thingsd)
    print(t.inserted_ids)
