
class chiper():
    def encrypt(m):
        cipher = ''
        for char in m:
            if not char.isalpha():
                continue
            char = char.upper()
            code = ord(char) + 1
            if code > ord('Z'):
                code = ord('A')
            cipher += chr(code)
        return(cipher)

    def decrypt(c):
        text = ''
        for char in c:
            if not char.isalpha():
                continue
            char = char.upper()
            code = ord(char) - 1
            if code < ord('A'):
                code = ord('Z')
            text += chr(code)
        return(text)


# Encrypting Caesar cipher
msg = input("Enter your message: ")
print(chiper.encrypt(msg))

# Caesar cipher - decrypting a message
code = input('Enter your cryptogram: ')
print(chiper.decrypt(code))