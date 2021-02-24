import CaesarCipher

def EncryptionWord(alphabet, keyWord, Word, n, lenKeyWord):
    for j in range(len(Word)):
        k = alphabet[keyWord[j % lenKeyWord]]
        Word[j] = CaesarCipher.EncryptionLetter(n, k, alphabet, Word[j])

def Encryption(alphabet, keyWord, text):
    keyWord = keyWord.lower()
    lenKeyWord = len(keyWord)
    n = len(alphabet) // 2
    for i in range(len(text)):
        if text[i] == ['|', 'n']:
            continue
        EncryptionWord(alphabet, keyWord, text[i], n, lenKeyWord)

 
def DecryptionWord(alphabet, keyWord, Word, n, lenKeyWord):
    for j in range(len(Word)):
        k = n - alphabet[keyWord[j % lenKeyWord]]
        Word[j] = CaesarCipher.EncryptionLetter(n, k, alphabet, Word[j])

def Decryption(alphabet, keyWord, text):
    keyWord = keyWord.lower()
    lenKeyWord = len(keyWord)
    n = len(alphabet) // 2
    for i in range(len(text)):
        if text[i] == ['|', 'n']:
            continue
        DecryptionWord(alphabet, keyWord, text[i], n, lenKeyWord)
