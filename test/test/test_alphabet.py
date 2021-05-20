import unittest
from alphabet import Alphabet
from alphabet import EnglishString

class AlphabetTest(unittest.TestCase):
	def _test_сommon(self, alph, en, direction):
		if   direction == 'checkNumToChars':
			for i in range(len(en)):
				self.assertEqual(alph[i], en[i])
		elif direction == 'checkCharsToNum':
			for i in range(len(en)):
				self.assertEqual(alph[en[i]], i)

	def _test_built_in_functions(self, testing_method, direction):
		alph = Alphabet()
		
		if   testing_method == 'small':
			alph.create_small()
			en = EnglishString.small()
		elif testing_method == 'smallAndBig':
			alph.create_small_and_big()
			en = EnglishString.small_and_big()
		elif testing_method == 'commonChars':
			alph.create_common_chars()
			en = EnglishString.common_chars()
		elif testing_method == 'create':
			en = EnglishString.small()
			alph.create(en)

		self._test_сommon(alph, en, direction)

	def test_create_small_pre_test(self):
		alph = Alphabet()
		alph.create_small()

		with self.assertRaises(KeyError):
			alph[69]
		with self.assertRaises(KeyError):
			alph["ad"]

	def test_create_small_num_to_chars(self):
		self._test_built_in_functions('small', 'checkNumToChars')

	def test_create_small_chars_to_num(self):
		self._test_built_in_functions('small', 'checkCharsToNum')

	def test_create_small_and_big_pre_test(self):
		alph = Alphabet()
		alph.create_small_and_big()
		with self.assertRaises(KeyError):
			alph[69]
		with self.assertRaises(KeyError):
			alph["ad"]

	def test_create_small_and_big_num_to_chars(self):
		self._test_built_in_functions('smallAndBig', 'checkNumToChars')

	def test_create_small_and_big_Chars_to_num(self):
		self._test_built_in_functions('smallAndBig', 'checkCharsToNum')

	def test_create_common_chars_pre_test(self):
		alph = Alphabet()
		alph.create_common_chars()
		with self.assertRaises(KeyError):
			alph[1000]
		with self.assertRaises(KeyError):
			alph["ad"]

	def test_create_common_chars_num_to_chars(self):
		self._test_built_in_functions('commonChars', 'checkNumToChars')

	def test_create_common_chars_chars_to_num(self):
		self._test_built_in_functions('commonChars', 'checkCharsToNum')

	def test_create_pre_test(self):
		alph = Alphabet()
		en = EnglishString.small()
		alph.create(en)

		with self.assertRaises(KeyError):
			alph[1000]
		with self.assertRaises(KeyError):
			alph["ad"]

	def test_create_num_to_chars(self):
		self._test_built_in_functions('create', 'checkNumToChars')

	def test_create_chars_to_num(self):
		self._test_built_in_functions('create', 'checkCharsToNum')
