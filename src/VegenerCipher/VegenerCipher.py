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
