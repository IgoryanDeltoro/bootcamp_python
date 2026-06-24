from recipe import Recipe

if __name__ == "__main__":

    cake = Recipe(
        name="Cake",
        cooking_lvl=3,
        cooking_time=60,
        ingredients=["flour", "sugar", "eggs"],
        description="Delicious chocolate cake",
        recipe_type="dessert"
    )

    toprint = str(cake)
    print(toprint)

