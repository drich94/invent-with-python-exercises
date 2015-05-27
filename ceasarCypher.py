# Caesar Cypher

import pyperclip
import random

#the string to be encrypted/decrypted
message = input('enter message: ')

#encryption key
key = input('enter key: ')
key = int(key)
#tells the program to set encrypt or decrypt
mode = input('select mode: ')

# every possible symbol that can be ecrypted

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
SYMBOLS = '01234567890!. ,<>?@#$%^&*='

# stores the encrypted/decrypted form of the message
translated = ''

#capitalize the string in message

message = message.upper()

#run the en/decryption code on each symbol in the message string
for symbol in message:
    if symbol in LETTERS:
        #get the encrypted number for this symbol
        num = LETTERS.find(symbol)
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key


        #incase num is larger than the length of letters/less than 0
        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)

        #add encrypted/decrypted number's symbol at the end of translated
        translated = translated + LETTERS[num]
     
    elif symbol in SYMBOLS:
        num2 = SYMBOLS.find(symbol)
        if mode == 'encrypt':
            num2 = num2 + key
        elif mode == 'decrypt':
            num2 = num2 - key

        if num2 >= len(SYMBOLS):
            num2 = num2 - len(SYMBOLS)
        elif num2 < 0:
            num2 = num2 + len(SYMBOLS)


        translated = translated + SYMBOLS[num2]



    else:
        #just add the symbol without encrypting/decrypting
        translated = translated + symbol


print(translated)

pyperclip.copy(translated)
