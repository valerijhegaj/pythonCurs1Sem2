import CaesarCipher

def calculationParametr(stat, frequency, shift):
    parametr = 0
    n = len(stat)
    for i in range(n):
        j = (i + shift) % n
        parametr += (stat[j] - frequency[i]) ** 2
    return parametr

def findShift(stat, frequency):
    shift = 0
    parametr = calculationParametr(stat, frequency, 0)
    for i in range(1, len(stat)):
        parametrLoc = calculationParametr(stat, frequency, i)
        if parametr > parametrLoc:
            parametr = parametrLoc
            shift = i
    return shift

def hack(alphabet, data, frequency):
    stat = [0] * (len(alphabet) // 2)
    n = len(data)
    for i in data:
        if alphabet.get(i.lower(), -1) == -1:
            continue
        stat[alphabet[i.lower()]] += 1
    for i in range(len(stat)):
        stat[i] /= n
    shift = findShift(stat, frequency)
    CaesarCipher.Decryption(shift, alphabet, data)
