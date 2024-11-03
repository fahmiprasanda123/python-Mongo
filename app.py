from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId  # Import ObjectId dari bson

app = Flask(__name__)

# Konfigurasi koneksi MongoDB
app.config["MONGO_URI"] = "mongodb://mongo:27017/mydatabase"
mongo = PyMongo(app)

@app.route('/items', methods=['GET'])
def get_items():
    try:
        items = mongo.db.items.find()
        items_list = [{**item, "_id": str(item["_id"])} for item in items]
        return jsonify(items_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/items', methods=['POST'])
def add_item():
    try:
        data = request.json
        mongo.db.items.insert_one(data)
        return jsonify(data), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/items/<id>', methods=['PUT'])
def update_item(id):
    try:
        data = request.json
        mongo.db.items.update_one({"_id": ObjectId(id)}, {"$set": data})  # Gunakan ObjectId dengan benar
        return jsonify({"message": "Item updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/items/<id>', methods=['DELETE'])
def delete_item(id):
    try:
        result = mongo.db.items.delete_one({"_id": ObjectId(id)})  # Gunakan ObjectId dengan benar
        if result.deleted_count > 0:
            return jsonify({"message": "Item deleted successfully"}), 200
        else:
            return jsonify({"error": "Item not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
