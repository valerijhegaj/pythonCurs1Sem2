import sys
import os
sys.path.append(os.path.join(sys.path[0], ".."))

from frontend import Interface

is_finish = 0

while not(is_finish):
    input_word = input().split()
    if input_word == []:
    	continue
    if input_word[0] == 'exit':
        is_finish = 1
    elif input_word[0] == 'caesar':
        if   input_word[1] == '-e':
            Interface.caesar_cipher_common(input_word[2], input_word[3], int(input_word[4]), 1, 0)
        elif input_word[1] == '-d':
            Interface.caesar_cipher_common(input_word[2], input_word[3], int(input_word[4]), 0, 0)
        elif input_word[1] == '-h':
        	Interface.caesar_cipher_hack(input_word[2], input_word[3])
        elif input_word[1] == '-ei':
            try:
                Interface.caesar_cipher_common(input_word[2], input_word[3], int(input_word[4]), 1, 1)
            except RuntimeError:
                print('Can\'t read this web-site')
        else:
            print('There is no such command')
    elif input_word[0] == 'vigener':
        if   input_word[1] == '-e':
            Interface.vegener_cipher_common(input_word[2], input_word[3], input_word[4], 1, 0)
        elif input_word[1] == '-d':
            Interface.vegener_cipher_common(input_word[2], input_word[3], input_word[4], 0, 0)
        elif input_word[1] == '-ei':
            try:
                Interface.vegener_cipher_common(input_word[2], input_word[3], input_word[4], 1, 1)
            except RuntimeError:
                print('Can\'t read this web-site')
        else:
            print('There is no such command')
    elif input_word[0] == 'vernam':
        if input_word[1] == '-e':
            Interface.vernam_common(input_word[2], input_word[3], 0, input_word[4], 1, 0)
        elif input_word[1] == '-eg':
            Interface.vernam_common(input_word[2], input_word[3], 1, input_word[4], 1, 0)
        elif input_word[1] == '-d':
            Interface.vernam_common(input_word[2], input_word[3], 0, input_word[4], 1, 0)
        elif input_word[1] == '-ei':
            try:
                Interface.vernam_common(input_word[2], input_word[3], 0, input_word[4], 1, 1)
            except RuntimeError:
                print('Can\'t read this web-site')
        elif input_word[1] == '-egi':
            try:
                Interface.vernam_common(input_word[2], input_word[3], 1, input_word[4], 1, 1)
            except RuntimeError:
                print('Can\'t read this web-site')   
        else:
            print('There is no such command')
    else:
        print('There is no such command')
