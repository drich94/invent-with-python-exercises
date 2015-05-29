import pyperclip
import random

message = input('string: ')
message = message.upper()

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
SYMBOLS = '01234567890!. ,<>?@#$%^&*='

for key in range(len(LETTERS)):
    translated = ''


    for symbol in message:
        
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = num - key

            if num < 0:
                    num = num + len(LETTERS)

            translated = translated + LETTERS[num]

        elif symbol in SYMBOLS:
            num2 = SYMBOLS.find(symbol)
            num2 = num2 - key

            if num2 < 0:
                    num2 = num2 + len(SYMBOLS)

            translated = translated + SYMBOLS[num2]


    print('key #%s: %s' % (key,translated))
                
