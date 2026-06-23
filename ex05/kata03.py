kata = "The right format"


def main():
    """
    This kata aligns to the right margin (>),
    total length 42, fill in the spaces with hyphens (-)
    """

    print(f"{kata:->42}", end="")


if __name__ == "__main__":
    main()
