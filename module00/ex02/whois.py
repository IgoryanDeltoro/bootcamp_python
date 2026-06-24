import sys


def main():

    args = sys.argv[1:]
    arg_len = len(args)

    if arg_len == 0:
        raise AssertionError("usage: python3 .whois.py <number>")

    if arg_len > 1:
        raise AssertionError("more than one argument is provided")

    try:
        num = int(args[0])

        if num == 0:
            print("I'm Zero.")
        elif num % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")

    except ValueError:
        raise AssertionError("argument is not an integer")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as error:
        print(f"AssertionError: {error}", file=sys.stderr)
        sys.exit(1)
