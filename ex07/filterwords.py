import sys
import string


def main():
    """
    This program takes a string S and an integer N as argument and
    prints the list of words in S that contains more than N
    non-punctuation characters.
    """

    args = sys.argv[1:]

    if len(args) != 2:
        print("Error: incorrect number of arguments")
        print("Usage: python3 filterwords.py <'Hello World!'> <3>")
        return

    try:
        S = args[0]
        N = int(args[1])

        if N < 1:
            raise ValueError()

        filtred = "".join(char for char in S if char not in string.punctuation)
        words = [word for word in filtred.split(" ") if len(word) > N]
        print(words)

    except ValueError:
        print("ERROR")


if __name__ == "__main__":
    main()
