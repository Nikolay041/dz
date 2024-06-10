# class Shoe:
#     def __init__(self, shoe_type, shoe_style, color, price, manufacturer, size):
#         self.shoe_type = shoe_type
#         self.shoe_style = shoe_style
#         self.color = color
#         self.price = price
#         self.manufacturer = manufacturer
#         self.size = size
#
#
# class ShoeController:
#     def __init__(self):
#         pass
#
#     def create_shoe(self, shoe_type, shoe_style, color, price, manufacturer, size):
#         return Shoe(shoe_type, shoe_style, color, price, manufacturer, size)
#
#
# class ShoeView:
#     def shoe_details(self, shoe):
#         print("Shoe Type: {}".format(shoe.shoe_type))
#         print("Shoe Style: {}".format(shoe.shoe_style))
#         print("Color: {}".format(shoe.color))
#         print("Price: {}".format(shoe.price))
#         print("Manufacturer: {}".format(shoe.manufacturer))
#         print("Size: {}".format(shoe.size))
#
#
# class ShoeModel:
#     def __init__(self):
#         self.shoe = None
#
#     def set_shoe(self, shoe):
#         self.shoe = shoe
#
#     def get_shoe(self):
#         return self.shoe
#
#
# if __name__ == '__main__':
#     shoe_controller = ShoeController()
#     shoe_model = ShoeModel()
#     shoe_view = ShoeView()
#
#     shoe = shoe_controller.create_shoe("men", "sneakers", "black", 50, "Adidas",
#                                        43)
#     shoe_model.set_shoe(shoe)
#
#     shoe_details = shoe_model.get_shoe()
#     shoe_view.shoe_details(shoe_details)


# class Recipe:
#     def __init__(self, name, author, recipe_type, description, video_link, ingredients, cuisine):
#         self.name = name
#         self.author = author
#         self.recipe_type = recipe_type
#         self.description = description
#         self.vide_link = video_link
#         self.ingredients = ingredients
#         self.cuisine = cuisine
#
#     def get_info(self):
#         return (f"Recipe: {self.name}\n Author: {self.author}\n Type: {self.recipe_type}\n "
#                 f"Description: {self.description}\n Video Link: {self.vide_link}\n "
#                 f"Ingredients: {', '.join(self.ingredients)}\n Cuisine: {self.cuisine}")
#
#
# class RecipeController:
#     def create_recipe(self, name, author, recipe_type, description, video_link, ingredients, cuisine):
#         recipe = Recipe(name, author, recipe_type, description, video_link, ingredients, cuisine)
#         return recipe
#
#
# class RecipeView:
#     def show_recipe(self, recipe):
#         print(recipe.get_info())
#
#
# controller = RecipeController()
# view = RecipeView()
#
# recipe_data = {
#     "name": "Jamie Oliver",
#     "author": "ItalianChef123",
#     "recipe_type": "main course",
#     "description": "Delicious pasta dish with bacon, eggs, and cheese.",
#     "video_link": "https://www.youtube.com/watch?v=3AAdKl1UYZs",
#     "ingredients": ["spaghetti", "bacon", "eggs", "parmesan cheese"],
#     "cuisine": "Italian"
# }
#
# recipe = controller.create_recipe(**recipe_data)
# view.show_recipe(recipe)




