import unittest
from alphabet import EnglishString

class EnglishTest(unittest.TestCase):
	english = 'abcdefghijklmnopqrstuvwxyz'
	
	def test_small(self):
		self.assertEqual(EnglishString.small(), self.english)

	def test_small_and_big(self):
		self.assertEqual(EnglishString.small_and_big(), self.english + self.english.upper())
