
alphabet = "abcdefghijklmnopqrstuvwxyz 0123456789:!?,.áéíóúý()"
from art import logo


def shift1():
    while True:
        try:
            shift = int(input("Type the shift number:\n")) - 1
            if 0 < shift < 49:
                return shift
            else:
                print("The number must be > 0 and < 49")
        except:
            print("It must be a number ofc")

def ceasar():
    encryptedword = ""
    if direction == "e" or direction == "encode":
        for x in text:
            test1 = alphabet.find(x)
            if test1 == -1:
                encryptedword += x
            elif (test1 + shift) > 49:
                encryptedword += alphabet[(test1 + shift) - 50]
            else:
                encryptedword += alphabet[(test1 + shift)]
        print(encryptedword)
    else:
        for x in text:
            test1 = alphabet.find(x)
            if alphabet.find(x) == -1:
                encryptedword += x
            else:
                encryptedword += alphabet[test1 - shift]
        print(encryptedword)


def direction1():
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction == "d" or direction == "decode":
            return direction
        elif direction == "e" or direction == "decode":
            return direction



def text1():
    text = input("Type your message:\n").lower()
    return text




if __name__ == '__main__':
    while True:
        print(logo)
        direction = direction1()
        text = text1()
        shift = shift1()
        ceasar()
        ancora = input("Try again?? Y N\n").lower()
        if ancora == "y":
            continue
        if ancora == "n":
            print("Goodbye")
            break
