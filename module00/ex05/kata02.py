kata = (2019, 9, 25, 3, 30)


def main():
    """
    This kata displays a date
    """

    year = kata[0]
    month = kata[1]
    day = kata[2]
    hour = kata[3]
    minute = kata[4]

    print(f"{month:02d}/{day:02d}/{year:04d} {hour:02d}:{minute:02d}")


if __name__ == "__main__":
    main()
