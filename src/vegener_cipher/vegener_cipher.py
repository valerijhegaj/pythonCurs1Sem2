from caesar_cipher import CaesarCipher

class VegenerCipher:
    def _commom_cryption(alphabet, key_word, text, is_en):
        ans = ''
        n = len(alphabet) // 2
        for i in range(len(text)):
            shift = alphabet[key_word[i % len(key_word)]]
            if not is_en:
                shift = n - shift
            ans += CaesarCipher._ecryption_char_with_big(n, shift, alphabet, text[i])
        return ans

    def encryption(alphabet, key_word, text):
        return VegenerCipher._commom_cryption(alphabet, key_word, text, 1)

    def decryption(alphabet, key_word, text):
        return VegenerCipher._commom_cryption(alphabet, key_word, text, 0)
