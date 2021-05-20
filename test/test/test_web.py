import unittest
from web import Web

class WebTest(unittest.TestCase):
	def test_web(self):
		reader = Web()
		try:
			text = reader.read('http://example.com')
		except RuntimeError('changing site'):
			self.assertEqual(1, 0)
		self.assertEqual(text, 'This domain is for use in illustrative examples in documents. You may use this\n    domain in literature without prior coordination or asking for permission.')

	def test_web_exeption(self):
		reader = Web()
		try:
			reader.read('http://vk.com/feed')
			self.assertEqual('сайт не поменялся(', 0)
		except RuntimeError:
			None