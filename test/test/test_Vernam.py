import unittest
from Vernam  		import Vernam
from alphabet       import alphabet

class VernamTest(unittest.TestCase):
	def test_VernamTestcommon(self):
		en = alphabet()
		en.createCommonChars()
		text = "the cipher is easy to understand and implement, but it resist"
		key  = "zhckubtraugskpzojezfppqclnonxufvmmspnbdfcuiiqmrvheqvyejxecdqx"
		text_ = Vernam.encryption(en, key, text)
		self.assertEqual(text, Vernam.decryption(en, key, text_))