import os
from pymongo import MongoClient
from pymongo.errors import PyMongoError
import sys

def update_view_count():
    try:
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
            
        print(f"Successfully updated views to {new_views}")
        return True

    except PyMongoError as e:
        print(f"MongoDB error: {e}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return False

if __name__ == "__main__":
    success = update_view_count()
    sys.exit(0 if success else 1)
