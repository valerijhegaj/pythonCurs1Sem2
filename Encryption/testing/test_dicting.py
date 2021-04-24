import unittest
from alphabet import dicting

class dictingTest(unittest.TestCase):
	def test_init(self):
		x = dicting.create("se")
		self.assertEqual(x, {"s": 0, "e": 1, 1: "e", 0: "s"})