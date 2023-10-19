from flask import Flask, jsonify, request
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
        "instructions": [
            "Boil pasta until al dente.",
            "In a saucepan, heat olive oil and sauté minced garlic.",
            "Add basil and tomato sauce to the pan.",
            "Serve sauce over cooked pasta and garnish with grated Parmesan cheese."
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
        "instructions": [
            "Roll out pizza dough and spread tomato sauce over it.",
            "Add mozzarella cheese, pepperoni, bell peppers, and onions as toppings.",
            "Bake in the oven until the crust is golden and the cheese is melted and bubbly."
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
        "instructions": [
            "Cook ground beef in a pan, seasoning it with taco seasoning.",
            "Warm tortillas in a dry skillet or microwave.",
            "Assemble tacos with cooked beef, lettuce, tomatoes, and sour cream."
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
        "instructions": [
            "Shape ground beef into patties and cook on a grill or stovetop.",
            "Toast burger buns on the grill.",
            "Assemble burgers with lettuce, tomatoes, cheese, ketchup, and mustard."
        ],
    },
    {
        "id": 5,
        "title": "Sushi Delight",
        "image": "sushi-image.jpg",
        "description": "Savor the flavors of fresh sushi rolls.",
        "foodType": "Japanese",
        "ingredients": ["Sushi Rice", "Nori Seaweed", "Fish", "Cucumber", "Avocado"],
        "instructions": [
            "Prepare sushi rice and season it with rice vinegar and sugar.",
            "Place a sheet of nori seaweed on a bamboo sushi rolling mat.",
            "Spread rice on the nori, add fish, cucumber, and avocado.",
            "Roll the sushi and cut it into bite-sized pieces."
        ],
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
        "instructions": [
            "Cook lasagna noodles until al dente.",
            "Brown ground beef in a skillet and mix with tomato sauce.",
            "Layer lasagna noodles with meat sauce, ricotta, and mozzarella cheese.",
            "Bake until cheese is bubbly and golden."
        ],
    },
    {
        "id": 7,
        "title": "Thai Green Curry",
        "image": "curry-image.jpg",
        "description": "A spicy and aromatic Thai dish with vegetables and chicken.",
        "foodType": "Thai",
        "ingredients": ["Chicken", "Coconut Milk", "Green Curry Paste", "Vegetables"],
        "instructions": [
            "Cook chicken in a pan until browned.",
            "Add coconut milk and green curry paste.",
            "Simmer with vegetables until cooked through."
        ],
    },
    {
        "id": 8,
        "title": "Mediterranean Salad",
        "image": "salad-image.jpg",
        "description": "A refreshing salad with olives, feta cheese, and fresh vegetables.",
        "foodType": "Mediterranean",
        "ingredients": ["Lettuce", "Olives", "Feta Cheese", "Cucumbers", "Tomatoes"],
        "instructions": [
            "Chop lettuce, olives, and cucumbers.",
            "Crumble feta cheese over the salad.",
            "Add diced tomatoes and drizzle with olive oil."
        ],
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
        "instructions": [
            "Mix dry ingredients and wet ingredients separately.",
            "Combine and bake until a toothpick comes out clean.",
            "Frost the cake with melted chocolate."
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
        "instructions": [
            "Cook pasta until al dente.",
            "Sauté chicken and garlic, then add cream and Parmesan cheese.",
            "Toss cooked pasta with the creamy sauce."
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
        "instructions": [
            "Cook lasagna noodles until al dente.",
            "Brown ground beef in a skillet and mix with tomato sauce.",
            "Layer lasagna noodles with meat sauce, ricotta, and mozzarella cheese.",
            "Bake until cheese is bubbly and golden."
        ],
    },
    {
        "id": 12,
        "title": "Thai Green Curry",
        "image": "curry-image.jpg",
        "description": "A spicy and aromatic Thai dish with vegetables and chicken.",
        "foodType": "Thai",
        "ingredients": ["Chicken", "Coconut Milk", "Green Curry Paste", "Vegetables"],
        "instructions": [
            "Cook chicken in a pan until browned.",
            "Add coconut milk and green curry paste.",
            "Simmer with vegetables until cooked through."
        ],
    },
    {
        "id": 13,
        "title": "Mediterranean Salad",
        "image": "salad-image.jpg",
        "description": "A refreshing salad with olives, feta cheese, and fresh vegetables.",
        "foodType": "Mediterranean",
        "ingredients": ["Lettuce", "Olives", "Feta Cheese", "Cucumbers", "Tomatoes"],
        "instructions": [
            "Chop lettuce, olives, and cucumbers.",
            "Crumble feta cheese over the salad.",
            "Add diced tomatoes and drizzle with olive oil."
        ],
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
        "instructions": [
            "Mix dry ingredients and wet ingredients separately.",
            "Combine and bake until a toothpick comes out clean.",
            "Frost the cake with melted chocolate."
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
        "instructions": [
            "Cook pasta until al dente.",
            "Sauté chicken and garlic, then add cream and Parmesan cheese.",
            "Toss cooked pasta with the creamy sauce."
        ],
    },
]


# Define a route to get all recipes
@app.route('/api/recipes', methods=['GET'])
def get_recipes():
    search_query = request.args.get('search', default=None, type=str)

    if search_query:
        # Filter the recipes based on the search query
        filtered_recipes = [recipe for recipe in recipe_list if search_query.lower() in recipe['title'].lower()]

        return jsonify(filtered_recipes)
    
    # If no search query is provided, return all recipes
    return jsonify(recipe_list)

@app.route('/api/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    recipe = next((item for item in recipe_list if item["id"] == recipe_id), None)
    if recipe:
        return jsonify(recipe)
    return jsonify({"message": "Recipe not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
