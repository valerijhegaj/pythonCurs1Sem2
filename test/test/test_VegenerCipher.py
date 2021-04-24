import unittest
from VegenerCipher  import VegenerCipher
from alphabet       import alphabet
from alphabet       import englishString

class VegenerCipherTest(unittest.TestCase):
    def commonTest(self, is_encry):
        alph = alphabet()
        alph.create(englishString.small().upper())
        if is_encry:
            encrypted = VegenerCipher.encryption(alph, "LEMON", "ATTACKATDAWN")
            self.assertEqual(encrypted, "LXFOPVEFRNHR")
        else:
            decrypted = VegenerCipher.decryption(alph, "LEMON", "LXFOPVEFRNHR")
            self.assertEqual(decrypted, "ATTACKATDAWN")

    def test_encryption(self):
        self.commonTest(1)

    def test_decryption(self):
        self.commonTest(0)