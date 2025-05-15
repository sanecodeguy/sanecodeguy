import os
from pymongo import MongoClient


client = MongoClient(os.getenv("MONGODB_URI"))
db = client["github_views"]
collection = db["profile_views"]


doc = collection.find_one({"username": "sanecodeguy"})
views = doc["views"] if doc else 0
new_views = views + 1


collection.update_one(
    {"username": "sanecodeguy"},
    {"$set": {"views": new_views}},
    upsert=True
)


with open("views.txt", "w") as f:
    f.write(str(new_views))
