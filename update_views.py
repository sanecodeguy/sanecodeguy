import os
from pymongo import MongoClient

client = MongoClient(os.getenv("MONGODB_URI"))
db = client["github_views"]
collection = db["profile_views"]

doc = collection.find_one({"username": "sanecodeguy"})
if not doc:
    collection.insert_one({"username": "sanecodeguy", "views": 0})
    views = 0
else:
    views = doc["views"]

collection.update_one(
    {"username": "sanecodeguy"},
    {"$set": {"views": views + 1}}
)

with open("views.txt", "w") as f:
    f.write(str(views + 1))
