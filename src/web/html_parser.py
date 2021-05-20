from lxml import etree
from io import StringIO, BytesIO

class Parser:
	def parse(self, data):
		parser = etree.HTMLParser()
		tree = etree.parse(StringIO(data), parser)
		paragraphs = tree.xpath('//p')
		parsed = ''
		for i in paragraphs:
			text_loc = i.text
			if (text_loc != None):
				parsed += text_loc
		return parsed
