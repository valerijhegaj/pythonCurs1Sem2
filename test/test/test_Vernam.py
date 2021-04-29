import unittest
from vernam  		import Vernam
from alphabet       import Alphabet

class VernamTest(unittest.TestCase):
	def test_vernam_test_common(self):
		en = Alphabet()
		en.create_common_chars()
		text = "the cipher is easy to understand and implement, but it resist"
		key  = "zhckubtraugskpzojezfppqclnonxufvmmspnbdfcuiiqmrvheqvyejxecdqx"
		text_ = Vernam.encryption(en, key, text)
		self.assertEqual(text, Vernam.decryption(en, key, text_))