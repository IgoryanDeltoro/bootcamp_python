kata = (19,42,21)

def main():
    """
    This program displays a tuple length
    """
    numbers_str = ", ".join(str(num) for num in kata)
    print(f"The {len(kata)} numbers are: {numbers_str}")

if __name__=="__main__":
    main()