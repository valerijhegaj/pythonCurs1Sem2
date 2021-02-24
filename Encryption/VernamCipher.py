import random

def Encryption(alphabet, key, text):
    n = len(alphabet) // 2
    for i in range(len(text)):
        k = alphabet[key[i]]
        t = alphabet[text[i]]
        text[i] = alphabet[(k ^ t) % n]
    
def Decryption(alphabet, key, text):
    Encryption(alphabet, key, text)

def GenerateKey(alphabet, l):
    ans = ''
    n = len(alphabet) // 2
    for i in range(l):
        j = random.randint(0, n - 1)
        ans += alphabet[j]
    return ans
