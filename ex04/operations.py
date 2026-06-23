import sys


def print_usage():
    """
    Prints the usage instructions for the program.
    """

    print("Usage: python operations.py <number1> <number2>")
    print("Example:")
    print("    python operations.py 10 3")


def calculate(a, b):
    """
    Performs and prints the mathematical operations.
    """
    print(f"Sum:            {a + b}")
    print(f"Difference:     {a - b}")
    print(f"Product:        {a * b}")

    if b == 0:
        print("Quotient:       ERROR (division by zero)")
        print("Remainder:      ERROR (modulo by zero)")
    else:
        print(f"Quotient:     {a / b}")
        print(f"Remainder:    {a % b}")


def main():
    args = sys.argv[1:]

    if len(args) == 0:
        print_usage()
        return
        
    if len(args) != 2:
        print("AssertionError: Either too many or too few arguments were provided")
        print_usage()
        return
    
    if not (args[0].lstrip('-').isdigit() and args[1].lstrip('-').isdigit()):
        print("AssertionError: only integers are allowed")
        print_usage()
        return
    
    try:
        a = int(args[0])
        b = int(args[1])

        calculate(a, b)
    except ValueError as error:
        print("AssertionError: ", error)

if __name__=="__main__":
    main()