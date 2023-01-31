
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def encrypt():
    encryptedword = ""

    for x in text:
        test1 = alphabet2.find(x)
        print(test1,x)
        if (test1 + shift) > 25:
            test2 = (test1 + shift) - 26
            encryptedword += alphabet2[test2]
        else:
            encryptedword += alphabet2[(test1 + shift)]
    print(encryptedword)

def decode():
    encryptedword = ""
    for x in text:
        test1 = alphabet2.find(x)
        test2 = test1 - shift
        encryptedword += alphabet2[test2]
    print(encryptedword)



if __name__ == '__main__':
    alphabet2 = ""
    for y in range(26):
        alphabet2 += alphabet[y]
    print(alphabet2)
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n")) -1
        if direction == "e" or direction == "encode":
            parola = encrypt()
        elif direction == "d" or direction == "decode":
            decode()
        ancora = input("Vuoi riprovare? Y N\n").lower()
        if ancora == "y":
            continue
        if ancora == "n":
            break



    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
