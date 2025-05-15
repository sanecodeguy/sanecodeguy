import os
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient(os.getenv("MONGODB_URI"))
db = client["github_views"]
collection = db["profile_views"]

# Get or initialize count
doc = collection.find_one({"username": "sanecodeguy"})
current_views = doc["views"] if doc else 0
new_views = current_views + 1

# Update database
collection.update_one(
    {"username": "sanecodeguy"},
    {"$set": {"views": new_views}},
    upsert=True
)

# Write to file
with open("views.txt", "w") as f:
    f.write(str(new_views))
