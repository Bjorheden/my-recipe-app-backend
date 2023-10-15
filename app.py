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
        "ingredients": [
            "Pasta",
            "Tomato Sauce",
            "Olive Oil",
            "Garlic",
            "Basil",
            "Parmesan Cheese",
        ],
    },
    {
        "id": 2,
        "title": "Homemade Pizza",
        "image": "pizza-image.jpg",
        "description": "Create the perfect pizza at home.",
        "foodType": "Italian",
        "ingredients": [
            "Pizza Dough",
            "Tomato Sauce",
            "Mozzarella Cheese",
            "Pepperoni",
            "Bell Peppers",
            "Onions",
        ],
    },
    {
        "id": 3,
        "title": "Tasty Tacos",
        "image": "taco-image.jpg",
        "description": "Spicy and savory tacos for dinner.",
        "foodType": "Mexican",
        "ingredients": [
            "Tortillas",
            "Ground Beef",
            "Taco Seasoning",
            "Lettuce",
            "Tomatoes",
            "Sour Cream",
        ],
    },
    {
        "id": 4,
        "title": "Burger Bliss",
        "image": "burger-image.jpg",
        "description": "Build your dream burger at home.",
        "foodType": "American",
        "ingredients": [
            "Burger Buns",
            "Ground Beef",
            "Lettuce",
            "Tomatoes",
            "Cheese",
            "Ketchup",
            "Mustard",
        ],
    },
    {
        "id": 5,
        "title": "Sushi Delight",
        "image": "sushi-image.jpg",
        "description": "Savor the flavors of fresh sushi rolls.",
        "foodType": "Japanese",
        "ingredients": ["Sushi Rice", "Nori Seaweed", "Fish", "Cucumber", "Avocado"],
    },
    {
        "id": 6,
        "title": "Classic Lasagna",
        "image": "lasagna-image.jpg",
        "description": "Layers of pasta, meat, and cheese in a rich tomato sauce.",
        "foodType": "Italian",
        "ingredients": [
            "Lasagna Noodles",
            "Ground Beef",
            "Ricotta Cheese",
            "Mozzarella Cheese",
            "Tomato Sauce",
        ],
    },
    {
        "id": 7,
        "title": "Thai Green Curry",
        "image": "curry-image.jpg",
        "description": "A spicy and aromatic Thai dish with vegetables and chicken.",
        "foodType": "Thai",
        "ingredients": ["Chicken", "Coconut Milk", "Green Curry Paste", "Vegetables"],
    },
    {
        "id": 8,
        "title": "Mediterranean Salad",
        "image": "salad-image.jpg",
        "description": "A refreshing salad with olives, feta cheese, and fresh vegetables.",
        "foodType": "Mediterranean",
        "ingredients": ["Lettuce", "Olives", "Feta Cheese", "Cucumbers", "Tomatoes"],
    },
    {
        "id": 9,
        "title": "Chocolate Cake",
        "image": "cake-image.jpg",
        "description": "Indulge in a rich and moist chocolate cake with chocolate frosting.",
        "foodType": "Dessert",
        "ingredients": [
            "Flour",
            "Sugar",
            "Cocoa Powder",
            "Eggs",
            "Butter",
            "Chocolate",
        ],
    },
    {
        "id": 10,
        "title": "Chicken Alfredo",
        "image": "alfredo-image.jpg",
        "description": "Creamy pasta with grilled chicken and parmesan cheese.",
        "foodType": "Italian",
        "ingredients": [
            "Fettuccine Pasta",
            "Chicken",
            "Cream",
            "Parmesan Cheese",
            "Garlic",
        ],
    },
    {
        "id": 11,
        "title": "Classic Lasagna",
        "image": "lasagna-image.jpg",
        "description": "Layers of pasta, meat, and cheese in a rich tomato sauce.",
        "foodType": "Italian",
        "ingredients": [
            "Lasagna Noodles",
            "Ground Beef",
            "Ricotta Cheese",
            "Mozzarella Cheese",
            "Tomato Sauce",
        ],
    },
    {
        "id": 12,
        "title": "Thai Green Curry",
        "image": "curry-image.jpg",
        "description": "A spicy and aromatic Thai dish with vegetables and chicken.",
        "foodType": "Thai",
        "ingredients": ["Chicken", "Coconut Milk", "Green Curry Paste", "Vegetables"],
    },
    {
        "id": 13,
        "title": "Mediterranean Salad",
        "image": "salad-image.jpg",
        "description": "A refreshing salad with olives, feta cheese, and fresh vegetables.",
        "foodType": "Mediterranean",
        "ingredients": ["Lettuce", "Olives", "Feta Cheese", "Cucumbers", "Tomatoes"],
    },
    {
        "id": 14,
        "title": "Chocolate Cake",
        "image": "cake-image.jpg",
        "description": "Indulge in a rich and moist chocolate cake with chocolate frosting.",
        "foodType": "Dessert",
        "ingredients": [
            "Flour",
            "Sugar",
            "Cocoa Powder",
            "Eggs",
            "Butter",
            "Chocolate",
        ],
    },
    {
        "id": 15,
        "title": "Chicken Alfredo",
        "image": "alfredo-image.jpg",
        "description": "Creamy pasta with grilled chicken and parmesan cheese.",
        "foodType": "Italian",
        "ingredients": [
            "Fettuccine Pasta",
            "Chicken",
            "Cream",
            "Parmesan Cheese",
            "Garlic",
        ],
    },
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
