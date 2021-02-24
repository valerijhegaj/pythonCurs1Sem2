def EncryptionLetter(n, k, alphabet, letter):
    if alphabet.get(letter.lower(), -1) == -1:
        return letter
    ans = alphabet[(alphabet[letter.lower()] + k) % n]
    if letter.isupper():
        ans = ans.upper()
    return ans

def Encryption(k, alphabet, text):
    n = len(alphabet) // 2
    for i in range(len(text)):
        text[i] = EncryptionLetter(n, k, alphabet, text[i])

def DecryptionLetter(n, k, alphabet, letter):
    EncryptionLetter(n, -k, alphabet, letter)

def Decryption(k, alphabet, text):
    Encryption(-k, alphabet, text)
