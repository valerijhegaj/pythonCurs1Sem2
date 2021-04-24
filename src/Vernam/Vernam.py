import random

class Vernam:
    def encryption(alphabet, key, text):
        ans = ''
        n = len(alphabet) // 2
        for i in range(len(text)):
            if text[i] in {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}:
                ans += text[i]
            else:
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
