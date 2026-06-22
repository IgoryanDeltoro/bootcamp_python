import sys
import string


def text_analyzer(text=None):
    """
    This function analyzes a given string and counts characters.

    It displays the total number of printable characters,
    as well as the count of upper-case letters, lower-case letters,
    punctuation marks, and spaces.

    If no text or None is provided, the user is prompted to type a string.
    If the argument is not a string, an error message is printed.
    """
    if text is None or text == "":
        text = input("What is the text to analyze?\n>>")

    if text.isdigit():
        print("AssertionError: argument is not a string")
        return
    
    total_chars = len(text)
    upper_count = sum(1 for char in text if char.isupper())
    lower_count = sum(1 for char in text if char.islower())
    punct_count = sum(1 for char in text if char in string.punctuation)
    space_count = sum(1 for char in text if char.isspace())
    print(f"The text contains {total_chars} printable character(s):")
    print(f"- {upper_count} upper letter(s)")
    print(f"- {lower_count} lower letter(s)")
    print(f"- {punct_count} punctuation mark(s)")
    print(f"- {space_count} space(s)")



if __name__=="__main__":
    args = sys.argv[1:]
    if len(args) == 1:
        text_analyzer(args[0])
    elif len(args) == 0:
        text_analyzer()
    else:
        print("AssertionError: too meny arguments!")
