from caesar_cipher.rss import RSS

class CaesarCipher:
    def _ecryption_char_with_big(n, key, alphabet, char):
        if alphabet.get(char, -1) == -1:
            return char
        return alphabet[(alphabet[char] + key) % n]

    def _ecryption_char(n, key, alphabet, char):
        if alphabet.get(char.lower(), -1) == -1:
            return char
        ans = alphabet[(alphabet[char.lower()] + key) % n]
        if char.isupper():
            ans = ans.upper()
        return ans

    def encryption(key, alphabet, text):
        n = len(alphabet) // 2
        ans = ''
        for i in range(len(text)):
            ans += CaesarCipher._ecryption_char(n, key, alphabet, text[i])
        return ans

    def decryption(key, alphabet, text):
        return CaesarCipher.encryption(-key, alphabet, text)
    
    def _count_text_frequency(alphabet, text):
        data = [0] * (len(alphabet) // 2)
        size = len(text)
        for i in text:
            if alphabet.get(i.lower(), -1) == -1:
                continue
            data[alphabet[i.lower()]] += 1
        for i in range(len(data)):
            data[i] /= size
        return data

    def _calculate_shift(data, frequency):
        shift = 0
        RSS_min = RSS.count(data[shift:] + data[:shift], frequency)
        for i in range(1, len(data)):
            RSS_loc = RSS.count(data[i:] + data[:i], frequency)
            if RSS_min > RSS_loc:
                RSS_min = RSS_loc
                shift = i
        return shift

    def hack(alphabet, frequency, text):
        data = CaesarCipher._count_text_frequency(alphabet, text)
        shift = CaesarCipher._calculate_shift(data, frequency)
        return CaesarCipher.decryption(shift, alphabet, text)
