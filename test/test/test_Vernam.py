import unittest
from Vernam  		import Vernam
from alphabet       import alphabet

class VernamTest(unittest.TestCase):
	def test_encryption(self):
		en = alphabet()
		en.createCommonChars()
		text = "the cipher is easy to understand and implement, but it resist"
		key  = "zhckubtraugskpzojezfppqclnonxufvmmspnbdfcuiiqmrvheqvyejxecdqx"
		self.assertEqual("kag:wjCwef(AyYDoBCKwbYepijFFeuiwXmFmWjpkjqemDFLOgqdOqx,gaqlce", Vernam.encryption(en, key, text))

	def test_decryption(self):
		en = alphabet()
		en.createCommonChars()
		text = "kag:wjCwef(AyYDoBCKwbYepijFFeuiwXmFmWjpkjqemDFLOgqdOqx,gaqlce"
		key  = "zhckubtraugskpzojezfppqclnonxufvmmspnbdfcuiiqmrvheqvyejxecdqx"
		self.assertEqual("the cipher is easy to understand and implement, but it resist", Vernam.decryption(en, key, text))
