
class chiper():
    abj = 'abcdeghijklmnopqrstuvwxyz'
    abx = abj.upper()
    def encrypt(m, k=1):
        cipher = ''
        cchar = ''
        for char in m:
            if char in list(chiper.abj):
                code = chiper.abj.index(char) + k
                if code > 24:
                    while code > 24:
                        code = code-25
                elif code < -25:
                    while code <- 25:
                        code = code+25
                cchar = chiper.abj[code]
            elif char in list(chiper.abx):
                code = chiper.abx.index(char) + k
                if code > 24:
                    while code > 24:
                        code = code-25
                elif code < -25:
                    while code <- 25:
                        code = code+25
                cchar = chiper.abx[code]
            else:
                cchar = char
            cipher += cchar
        return(cipher)

    def decrypt(m, k=1):
        text = ''
        for char in m:
            if char in list(chiper.abj):
                code = chiper.abj.index(char) - k
                if code > 24:
                    while code > 24:
                        code = code-25
                elif code < -25:
                    while code <- 25:
                        code = code+25
                cchar = chiper.abj[code]
            elif char in list(chiper.abx):
                code = chiper.abx.index(char) - k
                if code > 24:
                    while code > 24:
                        code = code-25
                elif code < -25:
                    while code <- 25:
                        code = code+25
                cchar = chiper.abx[code]
            else:
                cchar = char
            text += cchar
        return(text)


# Encrypting Caesar cipher
def enc():
    try:
        msg = input("Enter your message: ")
        key = (int(input("Enter your key: "))) or 1
        print(chiper.encrypt(msg, key))
    except ValueError:
        print("Please input number only for the key !")

# Caesar cipher - decrypting a message
def dec():
    try:
        chip = input('Enter your cryptogram: ')
        key = (int(input("Enter your key: "))) or 1
        print(chiper.decrypt(chip, key))
    except ValueError:
        print("Please input number only for the key !")


q = (input('(0) Exit, (1) Encrypt, (2) Decrypt (Default (1)): ')) or '1'
if q == '1':
    enc()
elif q == '2':
    dec()
elif q == '0':
    exit()
else:
    pass