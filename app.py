import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with your React app's Render URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.route('/api/data', methods=['GET'])
def get_data():
  try:
    documents = []
    # Fetch all documents from the collection
    for doc in collection.find():
      # Convert ObjectId to string for JSON compatibility
      doc['_id'] = str(doc['_id'])
      documents.append(doc)
    return jsonify(documents)
  except Exception as e:
    return jsonify({"error": str(e)}), 500

@app.route('/api/data', methods=['POST'])
def post_item():
  form_data = request.json
  if not form_data:
    return jsonify({'error': 'No data provided'}), 400
  collection.insert_one(form_data)
  return jsonify({'message': 'Data pushed successfully!'}), 201

@app.route("/api/data/<string:item_id>", methods=['PUT'])
def update_item(item_id):
  try:
    form_data = request.json
    print(f"Updated data {form_data}")
    result = collection.update_one({"_id": ObjectId(item_id)}, {"$set": form_data})
    if result.matched_count == 0:
      return jsonify({"error": "Item not found"}), 404
    return jsonify({"message": "Item updated successfully", "updated_filds": form_data}), 200
  except Exception as e:
     return jsonify({"error": str(e)})

@app.route("/api/data/<id>", methods=["DELETE"])
def delete_item(id):
  result = collection.delete_one({"_id": ObjectId(id)})
  if result.deleted_count == 1:
    return jsonify({"success": True, "message": "Deleted successfully"}), 200
  return jsonify({"duccess": False, "message": "Item not found"}), 400
