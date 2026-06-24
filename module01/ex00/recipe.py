import sys


class Recipe:
    def __init__(self, name: str, cooking_lvl: int, cooking_time: int, ingredients: list, description: list, recipe_type: str):
        """
        Initializes a Recipe object and strictly validates all fields.
        Only the description can be an empty string.
        """

        try:
            if not isinstance(name, str) or not name:
                raise TypeError("The recipe name must be a non-empty string.")
            
            if not isinstance(cooking_lvl, int):
                raise TypeError("Cooking level must be an integer.")
            if cooking_lvl < 1 or cooking_lvl > 5:
                raise ValueError("Cooking level must be in range from 1 to 5.")

            if not isinstance(cooking_time, int):
                raise TypeError("Cooking time must be an integer.")
            if cooking_time < 0:
                raise ValueError("Cooking time cannot be negative.")
            
            if not isinstance(ingredients, list) or not ingredients:
                raise TypeError("Ingredients must be a non-empty list of strings.")
            if not all(isinstance(ing, str) and ing for ing in ingredients):
                raise ValueError("Cooking time cannot be negative.")
            
            if not isinstance(description, str) or not description:
                raise TypeError("Description must be a string.")
            
            valid_type = ["starter", "lunch", "dessert"]
            if not isinstance(recipe_type, str) or recipe_type not in valid_type:
                raise ValueError(f"Recipe type must be one of the following: {valid_type}")

            self.name = name
            self.cooking_lvl = cooking_lvl
            self.cooking_time = cooking_time
            self.ingredients = ingredients
            self.description = description
            self.recipe_type = recipe_type
 
        except (TypeError, ValueError) as error:
            print(f"Initialization Error: {error}")
            sys.exit(1)
    
    def __str__(self):
        """Returns a string representation of the recipe."""
        txt = (
            f"Recipe for {self.name}:\n"
            f"- Type: {self.recipe_type}\n"
            f"- Cooking Level: {self.cooking_lvl}/5\n"
            f"- Cooking Time: {self.cooking_time} minutes\n"
            f"- Ingredients: {', '.join(self.ingredients)}\n"
        )
        if self.description:
            txt += f"- Description: {self.description}\n"
        return txt