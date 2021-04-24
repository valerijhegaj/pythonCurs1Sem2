import unittest
from CaesarCipher 	import CaesarCipher
from alphabet     	import englishString
from alphabet     	import alphabet
from CaesarCipher 	import RSS
from interaction 	import interaction

class CaesarCipherTest(unittest.TestCase):
	def deAndEncryption_test(self, is_encry):
		en = englishString.small()
		n = len(en)
		alph = alphabet()
		alph.createSmall()
		for i in range(n):
			if is_encry:
				encrypted = CaesarCipher.encryption(i, alph, en)
				self.assertEqual(encrypted, en[i:] + en[:i])
			else:
				decrypted = CaesarCipher.decryption(i, alph, en)
				self.assertEqual(decrypted, en[n - i:] + en[:n - i])

	def test_encryption(self):
		self.deAndEncryption_test(1);

	def test_decryption(self):
		self.deAndEncryption_test(0);

	def test_RSS(self):
		referenceValues = [1, 2, 3, 4, 5, 6]
		receivedValues  = [6, 5, 4, 3, 2, 1]
		self.assertEqual(RSS.count(referenceValues, referenceValues), 0)
		self.assertEqual(RSS.count(referenceValues, receivedValues), 70)

	def test_hack(self):
		en = englishString.small()
		n = len(en)
		alph = alphabet()
		alph.createSmall()
		text = interaction.read("test_analyth.txt")
		for i in range(n):
			_text = CaesarCipher.encryption(i, alph, text)
			self.assertEqual(text, CaesarCipher.hack(alph, alph.getFrequency(), _text))
	