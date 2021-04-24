from alphabet  		import alphabet
from interaction 	import interaction
from CaesarCipher 	import CaesarCipher
from VegenerCipher 	import VegenerCipher
from Vernam 		import Vernam

class interface:
	def CaesarCipherCommon(pathToRead, pathToWrite, key, is_encry):
		en = alphabet()
		en.createSmall()
		text = interaction.read(pathToRead)
		if is_encry:
			text = CaesarCipher.encryption(key, en, text)
		else:
			text = CaesarCipher.decryption(key, en, text)
		interaction.write(pathToWrite, text)

	def CaesarCipherHack(pathToRead, pathToWrite):
		en = alphabet()
		en.createSmall()
		frequency = en.getFrequency()
		text = interaction.read(pathToRead)
		text = CaesarCipher.hack(en, frequency, text)
		interaction.write(pathToWrite, text)

	def VegenerCipherCommon(pathToRead, pathToWrite, key, is_encry):
		en = alphabet()
		en.createSmallAndBig()
		text = interaction.read(pathToRead)
		if is_encry:
			text = VegenerCipher.encryption(en, key, text)
		else:
			text = VegenerCipher.decryption(en, key, text)
		interaction.write(pathToWrite, text)

	def VernamCommon(pathToRead, pathToKey, is_generate, pathToWrite, is_encry):
		en = alphabet()
		en.createCommonChars()
		text = interaction.read(pathToRead)

		if is_generate:
			l = len(text)
			key = Vernam.generateKey(en, l)
			interaction.write(pathToKey, key)
		else:
			key = interaction.read(pathToKey)

		if is_encry:
			text = Vernam.encryption(en, key, text)
		else:
			text = Vernam.decryption(en, key, text)

		interaction.write(pathToWrite, text)
