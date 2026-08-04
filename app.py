import os
from flask import Flask, jsonify
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

# Fetch URI from Render Environment
MONGO_URI = "MONGO_URI"
if not MONGO_URI:
    raise ValueError("MONGO_URI environment variable is missing!")

client = MongoClient(MONGO_URI)
db = client["school_db"]
collection = db["students"]

def format_doc(doc):
    if doc:
        doc["_id"] = str(doc["_id"])
    return doc

@app.route("/data", methods=["GET"])
def get_all_data():
    try:
        cursor = collection.find().limit(100)
        results = [format_doc(doc) for doc in cursor]
        return jsonify({"status": "success", "data": results}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
