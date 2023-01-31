
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt():
    encryptedword = ""

    for x in text:
        test1 = alphabet2.find(x)
        test2 = test1
        z = 0
        print(test1,x)
        if (test1 + shift) >= 26:
            while test2 < 26:
                test2 +=1
                z += 1
            z = (z - shift) * 1
            encryptedword += alphabet2[z]
        else:
            encryptedword += alphabet2[(test1 + shift)]

        print(encryptedword)
    print(encryptedword)

def decode():
    encryptedword = ""
    for x in text:
        test1 = alphabet2.find(x)
        test2 = test1
        z = 0
        if (test1 - shift) < 0:
            while test2 < 0:
                test2 += 1
                z += 1
            z = (z - shift)
            encryptedword += alphabet2[z]
        else:
            encryptedword += alphabet2[(test1 - shift)]

    print(encryptedword)



if __name__ == '__main__':
    alphabet2 = ""
    for y in range(26):
        alphabet2 += alphabet[y]
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        if direction == "e" or direction == "encode":
            parola = encrypt()
        elif direction == "d" or direction == "decode":
            decode()
        ancora = input("Vuoi riprovare? Y N\n").lower()
        if ancora == "y":
            continue
        if ancora == "n":
            break

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 