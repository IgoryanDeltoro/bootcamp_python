cookbook = {
    'sandwich': {
        'ingredients': ['ham,', 'bread,', 'tomatoes'],
        'meal': 'lunch',
        'prep_time': 10
    },
    'cake': {
        'ingredients': ['flour,', 'sugar', 'eggs'],
        "meal": "dessert",
        'prep_time': 60
    },
    "salad": {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 15
    },
    "soupe": {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 15
    }
}

Greeting = 'Welcome to the Python Cookbook !'
Options = """
List of available options:
  1: Add a recipe
  2: Delete a recipe
  3: Print a recipe
  4: Print the cookbook
  5: Quit
"""


def print_recipes():
    """Printing all recipe names"""

    for recipe in cookbook:
        print(f"{recipe}")


def print_recipe(recipe):
    """Printing a recipe name and its details"""

    r = cookbook[recipe]
    print(f"Recipe for {recipe}:")
    print(f"  Ingredients list: {r['ingredients']}.")
    print(f"  To be eaten for {r['meal']}.")
    print(f"  Takes {r['prep_time']} minutes of cooking.")


def delete_recipe(recipe):

    del cookbook[recipe]
    print(f"The recipe {recipe} was successfuly deleted.")


def add_recipe():
    """Adding a new recipe"""

    while True:
        recipe_name = input("\nEnter a name:\n>> ")
        if recipe_name == "":
            print("Please, enter recipe name.")
            continue

        ingredients = []
        while True:
            ingredient = input("\nEnter ingredients:\n>> ")
            if ingredient == "":
                break
            ingredients.append(ingredient)

        type = input("\nEnter a meal type:\n>> ")
        time = input("\nEnter a preparation time:\n>> ")
        if time.startswith('-'):
            print("Please enter a valid time in minutes.")
            continue

        cookbook[recipe_name] = {
            "ingredients": ingredients,
            "meal": type,
            "prep_time": time
        }

        print("The recipe was successfuly created.")
        return


def find_resipe():
    while True:
        name = input("\nPlease enter a recipe name to get its details:\n>> ")

        if name not in cookbook:
            print("There is no recipe with this name.")
            continue

        return name


def main():
    """
    Create a dictionary called cookbook. You will
    use this cookbook to store recipes.
    """

    print(Greeting)

    while True:
        print(Options)
        text = input("Please select an option:\n>> ")

        try:
            option = int(text)

            if option > 5 or option < 1:
                print("\nSorry, this option does not exist.")
                continue

            if option == 1:
                add_recipe()
            if option == 2:
                delete_recipe(find_resipe())
            elif option == 3:
                print_recipe(find_resipe())
            elif option == 4:
                print_recipes()
            elif option == 5:
                print("\nCookbook closed. Goodbye !")
                return

        except ValueError as error:
            print("Sorry, this option does not exist.")


if __name__ == "__main__":
    main()
