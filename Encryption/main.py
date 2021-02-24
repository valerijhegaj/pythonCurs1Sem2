import init
import construction
import readWrite
import CaesarCipher
import VigenerCipher
import VernamCipher
import hackСaesar

def CaesarEncryption(way, key):
    English = init.alphabetEnglish()
    data = readWrite.read(way)
    data = data.replace('\n', ' ')
    data = list(data)
    CaesarCipher.Encryption(key, English, data)
    readWrite.write(way, data)

def CaesarDecryption(way, key):
    English = init.alphabetEnglish()
    data = readWrite.read(way)
    data = list(data)
    CaesarCipher.Decryption(key, English, data)
    readWrite.write(way, data)


def VigenerEncryption(way, key):
    English = init.alphabetEnglish()
    data = readWrite.read(way)
    data = construction.deconstruction(data)
    VigenerCipher.Encryption(English, key, data)
    data = construction.construction(data)
    readWrite.write(way, data)

def VigenerDecryption(way, key):
    English = init.alphabetEnglish()
    data = readWrite.read(way)
    data = construction.deconstruction(data)
    VigenerCipher.Decryption(English, key, data)
    data = construction.construction(data)
    readWrite.write(way, data)


def VernamEncryption(way, wayToKey):
    English = init.commonAlphabetChars()
    data = readWrite.read(way)
    key = readWrite.read(wayToKey)
    data = list(data)
    VernamCipher.Encryption(English, key, data)
    readWrite.write(way, data)

def VernamEncryptionGenerate(way, wayToKey):
    English = init.commonAlphabetChars()
    data = readWrite.read(way)
    key = VernamCipher.GenerateKey(English, len(data))
    data = list(data)
    VernamCipher.Encryption(English, key, data)
    readWrite.write(way, data)
    readWrite.write(wayToKey, key)

def VernamEncryptionGenerateKey(way):
    English = init.commonAlphabetChars()
    data = readWrite.read(way)
    key = VernamCipher.GenerateKey(English, len(data))
    data = list(data)
    VernamCipher.Encryption(English, key, data)
    readWrite.write(way, data)
    return key

def VernamEncryptionKey(way, key):
    English = init.commonAlphabetChars()
    data = readWrite.read(way)
    data = list(data)
    VernamCipher.Encryption(English, key, data)
    readWrite.write(way, data)


def VernamDecryption(way, wayToKey):
    English = init.commonAlphabetChars()
    data = readWrite.read(way)
    data = list(data)
    key = readWrite.read(wayToKey)
    VernamCipher.Decryption(English, key, data)
    readWrite.write(way, data)

def VernamDecryptionKey(way, key):
    English = init.commonAlphabetChars()
    data = readWrite.read(way)
    data = list(data)
    VernamCipher.Decryption(English, key, data)
    readWrite.write(way, data)


def HackCaesar(way):
    English = init.alphabetEnglish()
    data = readWrite.read(way)
    data = list(data)
    hackСaesar.hack(English, data, init.frequencyEnglish())
    readWrite.write(way, data)
