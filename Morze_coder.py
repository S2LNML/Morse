latin_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
              'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
              'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
              'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
              'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
              'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
              '4': '....-', '5': '.....', '6': '-....', '7': '--...',
              '8': '---..', '9': '----.', '0': '-----', ',': '--..--',
              '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
              '(': '-.--.', ')': '-.--.-', '!': '--..--', ':': '---...',
              ';': '-.-.-.', '_': '..--.-', '+': '.-.-.', '"': '.-..-.'}


def encode_to_morse(text):
    text = text.upper().split()
    res = ""
    for word in text:
        res += " ".join([latin_dict[char] for char in word]) + " "
    return res


def main():
    s = ""
    while s != "exit":
        print(f"Закодированный текст: {encode_to_morse(input("Введите текст для кодирования в азбуку Морзе: "))}")
        print()
        s = input('Если желаете продолжить, нажмите Enter, иначе введите "exit": ')
        print("\n")

main()