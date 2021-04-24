import unittest
from alphabet import englishString

class englishTest(unittest.TestCase):
	english = 'abcdefghijklmnopqrstuvwxyz'
	
	def test_small(self):
		self.assertEqual(englishString.small(), self.english)

	def test_smallAndBig(self):
		self.assertEqual(englishString.smallAndBig(), self.english + self.english.upper())

	def test_smallAndBigPunctuation(self):
		self.assertEqual(englishString.commonChars(), self.english + self.english.upper() + ',.":;!?() \n' + "'")
