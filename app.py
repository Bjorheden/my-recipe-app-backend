from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Define the recipe list as a Python list
recipe_list = [
    {
        "id": 1,
        "title": "Delicious Pasta",
        "image": "pasta-image.jpg",
        "description": "A mouthwatering pasta recipe.",
        "foodType": "Italian",
    },
    {
        "id": 2,
        "title": "Homemade Pizza",
        "image": "pizza-image.jpg",
        "description": "Create the perfect pizza at home.",
        "foodType": "Italian",
    },
    {
        "id": 3,
        "title": "Tasty Tacos",
        "image": "taco-image.jpg",
        "description": "Spicy and savory tacos for dinner.",
        "foodType": "Mexican",
    },
    {
        "id": 4,
        "title": "Burger Bliss",
        "image": "burger-image.jpg",
        "description": "Build your dream burger at home.",
        "foodType": "American",
    },
    {
        "id": 5,
        "title": "Sushi Delight",
        "image": "sushi-image.jpg",
        "description": "Savor the flavors of fresh sushi rolls.",
        "foodType": "Japanese",
    },
    {
        "id": 6,
        "title": "Classic Lasagna",
        "image": "lasagna-image.jpg",
        "description": "Layers of pasta, meat, and cheese in a rich tomato sauce.",
        "foodType": "Italian",
    },
    {
        "id": 7,
        "title": "Thai Green Curry",
        "image": "curry-image.jpg",
        "description": "A spicy and aromatic Thai dish with vegetables and chicken.",
        "foodType": "Thai",
    },
    {
        "id": 8,
        "title": "Mediterranean Salad",
        "image": "salad-image.jpg",
        "description": "A refreshing salad with olives, feta cheese, and fresh vegetables.",
        "foodType": "Mediterranean",
    },
    {
        "id": 9,
        "title": "Chocolate Cake",
        "image": "cake-image.jpg",
        "description": "Indulge in a rich and moist chocolate cake with chocolate frosting.",
        "foodType": "Dessert",
    },
    {
        "id": 10,
        "title": "Chicken Alfredo",
        "image": "alfredo-image.jpg",
        "description": "Creamy pasta with grilled chicken and parmesan cheese.",
        "foodType": "Italian",
    },
    {
        "id": 11,
        "title": "Classic Lasagna",
        "image": "lasagna-image.jpg",
        "description": "Layers of pasta, meat, and cheese in a rich tomato sauce.",
        "foodType": "Italian",
    },
    {
        "id": 12,
        "title": "Thai Green Curry",
        "image": "curry-image.jpg",
        "description": "A spicy and aromatic Thai dish with vegetables and chicken.",
        "foodType": "Thai",
    },
    {
        "id": 13,
        "title": "Mediterranean Salad",
        "image": "salad-image.jpg",
        "description": "A refreshing salad with olives, feta cheese, and fresh vegetables.",
        "foodType": "Mediterranean",
    },
    {
        "id": 14,
        "title": "Chocolate Cake",
        "image": "cake-image.jpg",
        "description": "Indulge in a rich and moist chocolate cake with chocolate frosting.",
        "foodType": "Dessert",
    },
    {
        "id": 15,
        "title": "Chicken Alfredo",
        "image": "alfredo-image.jpg",
        "description": "Creamy pasta with grilled chicken and parmesan cheese.",
        "foodType": "Italian",
    }
]

# Define a route to get all recipes
@app.route('/api/recipes', methods=['GET'])
def get_recipes():
    return jsonify(recipe_list)

@app.route('/api/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    recipe = next((item for item in recipe_list if item["id"] == recipe_id), None)
    if recipe:
        return jsonify(recipe)
    return jsonify({"message": "Recipe not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
