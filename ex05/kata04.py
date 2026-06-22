kata = (0, 4, 132.42222, 10000, 12345.67)

def main():
    """
    """

    mod = kata[0]
    ex = kata[1]
    num1 = kata[2]
    num2 = kata[3]
    num3 = kata[4]

    print(f"module_{mod:02d}, ex_{ex:02d} : {num1:.2f}, {num2:.2e}, {num3:.2e}")

if __name__=="__main__":
    main()