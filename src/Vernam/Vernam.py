import random

class Vernam:
    def encryption(alphabet, key, text):
        ans = ''
        n = len(alphabet) // 2
        for i in range(len(text)):
            k = alphabet[key[i]]
            t = alphabet[text[i]]
            ans += alphabet[(k ^ t) % n]
        return ans

    def decryption(alphabet, key, text):
        return Vernam.encryption(alphabet, key, text)

    def generateKey(alphabet, l):
        ans = ''
        n = len(alphabet) // 2
        for i in range(l):
            j = random.randint(0, n - 1)
            ans += alphabet[j]
        return ans
