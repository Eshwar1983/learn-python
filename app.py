app = Flask(__name__)
CORS(app)

MONGO_URI = "mongodb+srv://eshwargowda19_db_user:DG6Pq4EMcwylcZK6@cluster0.8vevz6x.mongodb.net/?appName=Cluster0"
client = MongoClient(MONGO_URI)
db = client["known-person"]
collection = db["populur"]

@app.route('/api/data', methods=['GET'])
def get_data():
  try:
    documents = []
    # Fetch all documents from the collection
    for doc in collection.find():
      # Convert ObjectId to string for JSON compatibility
      doc['_id'] = str(doc['_id'])
      print(f"Items are adding+: {doc}")
      documents.append(doc)
    return jsonify(documents)
  except Exception as e:
    return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
  app.run(port=5000, debug=True)
