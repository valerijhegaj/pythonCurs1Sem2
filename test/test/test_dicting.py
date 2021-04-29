import unittest
from alphabet import Dicting

class DictingTest(unittest.TestCase):
	def test_init(self):
		x = Dicting.create("se")
		self.assertEqual(x, {"s": 0, "e": 1, 1: "e", 0: "s"})