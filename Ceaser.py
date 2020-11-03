# Caesar Cipher
import base64

MAX_KEY_SIZE = 47


def getMode():
    while True:
        print('Do you wish to encrypt, decrypt a message? or force a decryption')
        mode = input().lower()
        if mode in 'encrypt e decrypt d force f'.split():
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d" or "force" or "f".')


def getMessage():
    print('Enter your message:')
    return input()


def getKey():
    key = 0
    while True:
        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key


def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''

    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            translated += chr(num)
        else:
            translated += symbol
    return translated


mode = getMode()
message = getMessage()
if mode[0] != 'f':
    key = getKey()
    translated_message = getTranslatedMessage(mode, message, key)
    print('Your translated text is:')
    print(translated_message)
else:
    for x in range(0, MAX_KEY_SIZE):
        translated = getTranslatedMessage(mode, message, x)
        print(str(x) + "\t" + translated)

