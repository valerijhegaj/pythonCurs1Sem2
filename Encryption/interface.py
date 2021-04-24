import main

isFinish = 0
while not(isFinish):
    inputWord = input().split()
    if inputWord[0] == 'exit':
        isFinish = 1
    elif inputWord[0] == 'caesar':
        if inputWord[1] == '-e':
            main.CaesarEncryption(inputWord[2], int(inputWord[3]))
        elif inputWord[1] == '-d':
            main.CaesarDecryption(inputWord[2], int(inputWord[3]))
        else:
            print('there is no such command')
    elif inputWord[0] == 'HackCaesar':
        main.HackCaesar(inputWord[1])
    elif inputWord[0] == 'vigener':
        if inputWord[1] == '-e':
            main.VigenerEncryption(inputWord[2], inputWord[3])
        elif inputWord[1] == '-d':
            main.VigenerDecryption(inputWord[2], inputWord[3])
        else:
            print('there is no such command')
    elif inputWord[0] == 'vernam':
        if inputWord[1] == '-e':
            main.VernamEncryption(inputWord[2], inputWord[3])
        elif inputWord[1] == '-ek':
            main.VernamEncryptionKey(inputWord[2], inputWord[3])
        elif inputWord[1] == '-eg':
            main.VernamEncryptionGenerate(inputWord[2], inputWord[3])
        elif inputWord[1] == '-egk':
            print(main.VernamEncryptionGenerateKey(inputWord[2]))
        elif inputWord[1] == '-d':
            main.VernamDecryption(inputWord[2], inputWord[3])
        elif inputWord[1] == '-dk':
            main.VernamDecryptionKey(inputWord[2], inputWord[3])
        else:
            print('there is no such command')
    else:
        print('there is no such command')
