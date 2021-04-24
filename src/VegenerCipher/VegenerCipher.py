from CaesarCipher import CaesarCipher

class VegenerCipher:
    def _commomCryption(alphabet, keyWord, text, is_en):
        ans = ''
        n = len(alphabet) // 2
        for i in range(len(text)):
            shift = alphabet[keyWord[i % len(keyWord)]]
            if not is_en:
                shift = n - shift
            ans += CaesarCipher._ecryptionCharWithBig(n, shift, alphabet, text[i])
        return ans

    def encryption(alphabet, keyWord, text):
        return VegenerCipher._commomCryption(alphabet, keyWord, text, 1)

    def decryption(alphabet, keyWord, text):
        return VegenerCipher._commomCryption(alphabet, keyWord, text, 0)






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
