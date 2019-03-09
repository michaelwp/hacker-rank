
class chiper():
    abj = 'abcdeghijklmnopqrstuvwxyz'
    abx = abj.upper()
    def encrypt(m, k=1):
        cipher = ''
        for char in m:
            if char in list(chiper.abj):
                code = chiper.abj.index(char) + k
                if code > 24:
                    code = code-25
                elif code < -25:
                    code = code+25
                cchar = chiper.abj[code]
            elif char in list(chiper.abx):
                code = chiper.abx.index(char) + k
                if code > 24:
                    code = code-25
                elif code < -25:
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
                    code = code-25
                elif code < -25:
                    code = code+25
                cchar = chiper.abj[code]
            elif char in list(chiper.abx):
                code = chiper.abx.index(char) - k
                if code > 24:
                    code = code-25
                elif code < -25:
                    code = code+25
                cchar = chiper.abx[code]
            else:
                cchar = char
            text += cchar
        return(text)


# Encrypting Caesar cipher
msg = input("Enter your message: ")
key = int(input("Enter your key: ")) 
print(chiper.encrypt(msg, key))

# Caesar cipher - decrypting a message
chip = input('Enter your cryptogram: ')
print(chiper.decrypt(chip, key))