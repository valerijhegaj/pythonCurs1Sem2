import unittest
from caesar_cipher 	import CaesarCipher
from alphabet     	import EnglishString
from alphabet     	import Alphabet
from caesar_cipher 	import RSS
from interaction 	import Interaction

class CaesarCipherTest(unittest.TestCase):
	def _test_de_and_encryption(self, is_encry):
		en = EnglishString.small()
		n = len(en)
		alph = Alphabet()
		alph.create_small()
		for i in range(n):
			if is_encry:
				encrypted = CaesarCipher.encryption(i, alph, en)
				self.assertEqual(encrypted, en[i:] + en[:i])
			else:
				decrypted = CaesarCipher.decryption(i, alph, en)
				self.assertEqual(decrypted, en[n - i:] + en[:n - i])

	def test_encryption(self):
		self._test_de_and_encryption(1);

	def test_decryption(self):
		self._test_de_and_encryption(0);

	def test_RSS(self):
		reference_values = [1, 2, 3, 4, 5, 6]
		received_values  = [6, 5, 4, 3, 2, 1]
		self.assertEqual(RSS.count(reference_values, reference_values), 0)
		self.assertEqual(RSS.count(reference_values, received_values), 70)

	def test_hack(self):
		en = EnglishString.small()
		n = len(en)
		alph = Alphabet()
		alph.create_small()
		reader = Interaction()
		text = reader.read("test_analyth.txt")
		for i in range(n):
			_text = CaesarCipher.encryption(i, alph, text)
			self.assertEqual(text, CaesarCipher.hack(alph, alph.get_frequency(), _text))
	