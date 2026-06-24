import sys


def reverse_words():

    if len(sys.argv) < 2:
        print("Usage: python3 exec.py 'Hello World'")
        return

    args = sys.argv[1:]
    orrigin_str = " ".join(args)
    rev_string = orrigin_str[::-1]
    result = rev_string.swapcase()
    print(result)


if __name__ == "__main__":
    reverse_words()
