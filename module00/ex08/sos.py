import sys
import string


MORSE_CODE_DICT = {
    'A': '.-',   'B': '-...',
    'C': '-.-.', 'D': '-..',    'E': '.',
    'F': '..-.', 'G': '--.',    'H': '....',
    'I': '..',   'J': '.---',   'K': '-.-',
    'L': '.-..', 'M': '--',     'N': '-.',
    'O': '---',  'P': '.--.',   'Q': '--.-',
    'R': '.-.',  'S': '...',    'T': '-',
    'U': '..-',  'V': '...-',   'W': '.--',
    'X': '-..-', 'Y': '-.--',   'Z': '--..',
    '1': '.----',    '2': '..---',  '3': '...--',
    '4': '....-',    '5': '.....',  '6': '-....',
    '7': '--...',    '8': '---..',  '9': '----.',
    '0': '-----',    ' ': '/',
}


def main():
    args = sys.argv[1:]

    if len(args) == 0:
        return

    if len(args) > 1:
        text = " ".join(char for char in args).upper()
    else:
        text = args[0].upper()

    if any(char in string.punctuation for char in text):
        print("ERROR")
        return

    result = "".join(MORSE_CODE_DICT[char] for char in text)
    print(result)


if __name__ == "__main__":
    main()
