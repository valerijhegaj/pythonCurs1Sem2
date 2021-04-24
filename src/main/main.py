import sys
import os
sys.path.append(os.path.join(sys.path[0], ".."))

from frontend import interface

isFinish = 0

while not(isFinish):
    inputWord = input().split()
    if inputWord == []:
    	continue
    if inputWord[0] == 'exit':
        isFinish = 1
    elif inputWord[0] == 'caesar':
        if   inputWord[1] == '-e':
            interface.CaesarCipherCommon(inputWord[2], inputWord[3], int(inputWord[4]), 1)
        elif inputWord[1] == '-d':
            interface.CaesarCipherCommon(inputWord[2], inputWord[3], int(inputWord[4]), 0)
        elif inputWord[1] == '-h':
        	interface.CaesarCipherHack(inputWord[2], inputWord[3])
        else:
            print('There is no such command')
    elif inputWord[0] == 'vigener':
        if   inputWord[1] == '-e':
            interface.VegenerCipherCommon(inputWord[2], inputWord[3], inputWord[4], 1)
        elif inputWord[1] == '-d':
            interface.VegenerCipherCommon(inputWord[2], inputWord[3], inputWord[4], 0)
        else:
            print('There is no such command')
    elif inputWord[0] == 'vernam':
        if inputWord[1] == '-e':
            interface.VernamCommon(inputWord[2], inputWord[3], 0, inputWord[4], 1)
        elif inputWord[1] == '-eg':
            interface.VernamCommon(inputWord[2], inputWord[3], 1, inputWord[4], 1)
        elif inputWord[1] == '-d':
            interface.VernamCommon(inputWord[2], inputWord[3], 0, inputWord[4], 1)
        else:
            print('There is no such command')
    else:
        print('There is no such command')
