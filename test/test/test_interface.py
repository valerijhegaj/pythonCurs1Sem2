import unittest
from frontend 		import interface
from alphabet		import alphabet
from interaction 	import interaction
from CaesarCipher 	import CaesarCipher
from VegenerCipher 	import VegenerCipher
from Vernam 		import Vernam

class interfaceTest(unittest.TestCase):
	def interfaceCaesarCipherCommon(self, is_encry):
		text = interaction.read('test_read3.txt')
		interaction.write('test_CaesarCipher.txt', text)
		interface.CaesarCipherCommon('test_CaesarCipher.txt', 'test_CaesarCipher.txt', 10, is_encry)
		en = alphabet()
		en.createSmall()
		if is_encry:
			text = CaesarCipher.encryption(10, en, text)
		else:
			text = CaesarCipher.decryption(10, en, text)
		self.assertEqual(text, interaction.read('test_CaesarCipher.txt'))

	def test_interfaceCaesarCipherEncryption(self):
		self.interfaceCaesarCipherCommon(1)

	def test_interfaceCaesarCipherDecryption(self):
		self.interfaceCaesarCipherCommon(0)

	def test_interfaceCaesarHack(self):
		self.interfaceCaesarCipherCommon(1)
		interface.CaesarCipherHack('test_CaesarCipher.txt', 'test_CaesarCipher.txt')
		self.assertEqual(interaction.read('test_read3.txt'), interaction.read('test_CaesarCipher.txt'))

	def interfaceVegenerCipherCommon(self, is_encry):
		text = interaction.read('test_read3.txt')
		interaction.write('test_VegenerCipher.txt', text)
		interface.VegenerCipherCommon('test_VegenerCipher.txt', 'test_VegenerCipher.txt', "python", is_encry)
		en = alphabet()
		en.createSmallAndBig()
		if is_encry:
			text = VegenerCipher.encryption(en, "python", text)
		else:
			text = VegenerCipher.decryption(en, "python", text)
		self.assertEqual(text, interaction.read('test_VegenerCipher.txt'))

	def test_interfaceVegenerCipherEncryption(self):
		self.interfaceVegenerCipherCommon(1)

	def test_interfaceVegenerCipherDecryption(self):
		self.interfaceVegenerCipherCommon(0)

	def interfaceVernamCommon(self, is_generate, is_encry):
		text = interaction.read('test_VernamCipher.txt')
		en = alphabet()
		en.createCommonChars()
		interface.VernamCommon('test_VernamCipher.txt', 'test_VernamKey.txt', is_generate, 'test_VernamCipher.txt', is_encry)
		
		key = interaction.read('test_VernamKey.txt')

		if is_encry:
			text = Vernam.encryption(en, key, text)
		else:
			text = Vernam.decryption(en, key, text)
		self.assertEqual(text, interaction.read('test_VernamCipher.txt'))

	def test_interfaceVernamGenerate(self):
		self.interfaceVernamCommon(1, 1)
		self.interfaceVernamCommon(0, 0)

	def test_interfaceVernamEncryption(self):
		self.interfaceVernamCommon(0, 1)

	def test_interfaceVernamDecryption(self):
		self.interfaceVernamCommon(0, 0)
