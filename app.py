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

if __name__ == '__main__':
    app.run(debug=True)
