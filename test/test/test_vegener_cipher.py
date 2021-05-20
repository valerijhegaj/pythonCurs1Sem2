import unittest
from vegener_cipher import VegenerCipher
from alphabet       import Alphabet
from alphabet       import EnglishString

class VegenerCipherTest(unittest.TestCase):
    def common_test(self, is_encry):
        alph = Alphabet()
        alph.create(EnglishString.small().upper())
        if is_encry:
            encrypted = VegenerCipher.encryption(alph, "LEMON", "ATTACKATDAWN")
            self.assertEqual(encrypted, "LXFOPVEFRNHR")
        else:
            decrypted = VegenerCipher.decryption(alph, "LEMON", "LXFOPVEFRNHR")
            self.assertEqual(decrypted, "ATTACKATDAWN")

    def test_encryption(self):
        self.common_test(1)

    def test_decryption(self):
        self.common_test(0)