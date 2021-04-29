from alphabet  			import Alphabet
from interaction 		import Interaction
from caesar_cipher 		import CaesarCipher
from vegener_cipher 	import VegenerCipher
from vernam 			import Vernam

class Interface:
	def caesar_cipher_common(path_to_read, path_to_write, key, is_encry):
		en = Alphabet()
		en.create_small()
		text = Interaction.read(path_to_read)
		if is_encry:
			text = CaesarCipher.encryption(key, en, text)
		else:
			text = CaesarCipher.decryption(key, en, text)
		Interaction.write(path_to_write, text)

	def caesar_cipher_hack(path_to_read, path_to_write):
		en = Alphabet()
		en.create_small()
		frequency = en.get_frequency()
		text = Interaction.read(path_to_read)
		text = CaesarCipher.hack(en, frequency, text)
		Interaction.write(path_to_write, text)

	def vegener_cipher_common(path_to_read, path_to_write, key, is_encry):
		en = Alphabet()
		en.create_small_and_big()
		text = Interaction.read(path_to_read)
		if is_encry:
			text = VegenerCipher.encryption(en, key, text)
		else:
			text = VegenerCipher.decryption(en, key, text)
		Interaction.write(path_to_write, text)

	def vernam_common(path_to_read, path_to_key, is_generate, path_to_write, is_encry):
		en = Alphabet()
		en.create_common_chars()
		text = Interaction.read(path_to_read)

		if is_generate:
			l = len(text)
			key = Vernam.generate_key(en, l)
			Interaction.write(path_to_key, key)
		else:
			key = Interaction.read(path_to_key)

		if is_encry:
			text = Vernam.encryption(en, key, text)
		else:
			text = Vernam.decryption(en, key, text)

		Interaction.write(path_to_write, text)
