import unittest
from frontend 		import Interface
from alphabet		import Alphabet
from interaction 	import Interaction
from caesar_cipher 	import CaesarCipher
from vegener_cipher import VegenerCipher
from vernam 		import Vernam

class InterfaceTest(unittest.TestCase):
	def interface_caesar_cipher_common(self, is_encry):
		reader = Interaction()
		text = reader.read('test_read3.txt')
		reader.write('test_CaesarCipher.txt', text)
		Interface.caesar_cipher_common('test_CaesarCipher.txt', 'test_CaesarCipher.txt', 10, is_encry, 0)
		en = Alphabet()
		en.create_small()
		if is_encry:
			text = CaesarCipher.encryption(10, en, text)
		else:
			text = CaesarCipher.decryption(10, en, text)
		self.assertEqual(text, reader.read('test_CaesarCipher.txt'))

	def test_interface_caesar_cipher_encryption(self):
		self.interface_caesar_cipher_common(1)

	def test_interface_caesar_cipher_decryption(self):
		self.interface_caesar_cipher_common(0)

	def test_InterfaceCaesarHack(self):
		reader = Interaction()
		self.interface_caesar_cipher_common(1)
		Interface.caesar_cipher_hack('test_CaesarCipher.txt', 'test_CaesarCipher.txt')
		self.assertEqual(reader.read('test_read3.txt'), reader.read('test_CaesarCipher.txt'))

	def interface_vegener_cipher_common(self, is_encry):
		reader = Interaction()
		text = reader.read('test_read3.txt')
		reader.write('test_VegenerCipher.txt', text)
		Interface.vegener_cipher_common('test_VegenerCipher.txt', 'test_VegenerCipher.txt', "python", is_encry, 0)
		en = Alphabet()
		en.create_small_and_big()
		if is_encry:
			text = VegenerCipher.encryption(en, "python", text)
		else:
			text = VegenerCipher.decryption(en, "python", text)
		self.assertEqual(text, reader.read('test_VegenerCipher.txt'))

	def test_InterfaceVegenerCipherEncryption(self):
		self.interface_vegener_cipher_common(1)

	def test_InterfaceVegenerCipherDecryption(self):
		self.interface_vegener_cipher_common(0)

	def interface_vernam_common(self, is_generate, is_encry):
		reader = Interaction()
		text = reader.read('test_VernamCipher.txt')
		en = Alphabet()
		en.create_common_chars()
		Interface.vernam_common('test_VernamCipher.txt', 'test_VernamKey.txt', is_generate, 'test_VernamCipher.txt', is_encry, 0)
		
		key = reader.read('test_VernamKey.txt')

		if is_encry:
			text = Vernam.encryption(en, key, text)
		else:
			text = Vernam.decryption(en, key, text)
		self.assertEqual(text, reader.read('test_VernamCipher.txt'))

	def test_InterfaceVernamGenerate(self):
		self.interface_vernam_common(1, 1)
		self.interface_vernam_common(0, 0)

	def test_InterfaceVernamEncryption(self):
		self.interface_vernam_common(0, 1)

	def test_InterfaceVernamDecryption(self):
		self.interface_vernam_common(0, 0)
