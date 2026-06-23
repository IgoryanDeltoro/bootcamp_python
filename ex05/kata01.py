kata = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}


def main():
    """
    The kata variable is always a dictionary
    and can only be filled with strings
    """

    for language, creator in kata.items():
        print(f"{language} was created by {creator}")


if __name__ == "__main__":
    main()
