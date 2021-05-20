import unittest
from web import Parser

class ParserTest(unittest.TestCase):
	def test_parse_html(self):
		x = Parser()
		f = open('test_parser.html')
		text = f.read()
		f.close()
		self.assertEqual(x.parse(text), 'This domain is for use in illustrative examples in documents. You may use this domain in literature without prior coordination or asking for permission.')