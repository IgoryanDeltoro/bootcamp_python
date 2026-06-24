import random


def greed_user():
    print("This is an interactive guessing game!")
    print(f"You have to enter a number between 1 and 99"
          f" to find out the secret number.")
    print("Type 'exit' to end the game.")
    print("Good luck!")


def game(rand_num, attempt_number):

    try:
        while True:
            text = input("What's your guess between 1 and 99?\n>> ")
            if text.strip().lower() == "exit":
                print("Goodbye!")
                return

            num = int(text)
            if num < 1 or num > 99:
                print("\nIncorrect number.")
                continue

            attempt_number += 1

            if num < rand_num:
                print("Too low!")
            elif num > rand_num:
                print("Too high!")
            else:
                if num == 42 and attempt_number == 1:
                    print(f"The answer to the ultimate question of life,"
                          f" the universe and everything is 42.")
                    print("Congratulations! You got it on your first try!\n")
                else:
                    print("Congratulations, you've got it!")
                    print(f"You won in {attempt_number} attempts!\n")
                rand_num = random.randint(1, 99)
                attempt_number = 0

    except ValueError:
        print("\nIncorrect number.")
        game(rand_num, attempt_number)


def main():
    """
    This is an interactive guessing game.
    """

    greed_user()

    rand_num = random.randint(1, 99)
    attempt_number = 0

    game(rand_num, attempt_number)


if __name__ == "__main__":
    main()
