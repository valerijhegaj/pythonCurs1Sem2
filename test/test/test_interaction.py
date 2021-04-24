import unittest
from interaction 	import interaction
from alphabet 		import alphabet

class interactionTest(unittest.TestCase):
	def test_read(self):
		test_read1 = interaction.read("test_read1.txt")
		self.assertEqual(test_read1, "Hello world!")

		test_read2 = interaction.read("test_read2.txt")
		#длинная строчка файла
		self.assertEqual(test_read2, "Sys is a built-in Python module that contains parameters specific to the system i.e. it contains variables and methods that interact with the interpreter and are also governed by it.")

	def test_write(self):
		text = interaction.read("test_read3.txt")
		interaction.write("test_write1.txt", text)
		self.assertEqual(text, interaction.read("test_write1.txt"))