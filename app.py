from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from decouple import config

app = Flask(__name__)
CORS(app)

mongo_uri = config('MONGO_URI')

# Initialize a MongoDB client
client = MongoClient(mongo_uri)
db = client['recipe-app']  # Replace with your database name
collection = db['recipes']  # Replace with your collection name

# Define a route to get all recipes
@app.route('/api/recipes', methods=['GET'])
def get_recipes():
    search_query = request.args.get('search', default=None, type=str)

    if search_query:
        # Use MongoDB's aggregation to search for recipes
        pipeline = [
            {
                "$match": {
                    "title": {"$regex": search_query, "$options": "i"}
                }
            }
        ]
        filtered_recipes = list(collection.aggregate(pipeline))

        return jsonify(filtered_recipes)

    # If no search query is provided, return all recipes
    all_recipes = list(collection.find({}))
    return jsonify(all_recipes)

# Define a route to get a recipe by its integer ID
@app.route('/api/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    recipe = collection.find_one({"_id": recipe_id})

    if recipe:
        return jsonify(recipe)

    return jsonify({"message": "Recipe not found"}), 404

@app.route('/api/recipes', methods=['POST'])
def add_recipe():
    # Get the request data from the frontend
    recipe_data = request.get_json()

    # Query the collection to get the count of documents
    count = collection.count_documents({})

    # Calculate the next custom _id
    next_id = count + 1

    # Add the custom _id to the recipe data
    recipe_data["_id"] = next_id

    # Insert the new recipe into the collection
    collection.insert_one(recipe_data)

    # Return the ID of the newly added recipe
    return jsonify({"message": "Recipe added successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)
