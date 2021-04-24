import unittest
from interaction import interaction
from alphabet import alphabet

class interactionTest(unittest.TestCase):
	def test_read(self):
		test_read1 = interaction.read("testing/test_read1.txt")
		self.assertEqual(test_read1, "Hello world!")
