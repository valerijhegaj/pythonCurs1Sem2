import unittest
from alphabet import alphabet
from alphabet import englishString

class alphabetTest(unittest.TestCase):
	def _testCommon(self, alph, en, direction):
		if   direction == 'checkNumToChars':
			for i in range(len(en)):
				self.assertEqual(alph[i], en[i])
		elif direction == 'checkCharsToNum':
			for i in range(len(en)):
				self.assertEqual(alph[en[i]], i)

	def _testBuiltInFunctions(self, testingMethod, direction):
		alph = alphabet()
		
		if   testingMethod == 'small':
			alph.createSmall()
			en = englishString.small()
		elif testingMethod == 'smallAndBig':
			alph.createSmallAndBig()
			en = englishString.smallAndBig()
		elif testingMethod == 'commonChars':
			alph.createCommonChars()
			en = englishString.commonChars()
		elif testingMethod == 'create':
			en = englishString.small()
			alph.create(en)

		self._testCommon(alph, en, direction)

	def test_createSmallPreTest(self):
		alph = alphabet()
		alph.createSmall()

		with self.assertRaises(KeyError):
			alph[69]
		with self.assertRaises(KeyError):
			alph["ad"]

	def test_createSmallNumToChars(self):
		self._testBuiltInFunctions('small', 'checkNumToChars')

	def test_createSmallCharsToNum(self):
		self._testBuiltInFunctions('small', 'checkCharsToNum')

	def test_createSmallAndBigPreTest(self):
		alph = alphabet()
		alph.createSmallAndBig()
		with self.assertRaises(KeyError):
			alph[69]
		with self.assertRaises(KeyError):
			alph["ad"]

	def test_createSmallAndBigNumToChars(self):
		self._testBuiltInFunctions('smallAndBig', 'checkNumToChars')

	def test_createSmallAndBigCharsToNum(self):
		self._testBuiltInFunctions('smallAndBig', 'checkCharsToNum')

	def test_createCommonCharsPreTest(self):
		alph = alphabet()
		alph.createCommonChars()
		with self.assertRaises(KeyError):
			alph[1000]
		with self.assertRaises(KeyError):
			alph["ad"]

	def test_createCommonCharsNumToChars(self):
		self._testBuiltInFunctions('commonChars', 'checkNumToChars')

	def test_createCommonCharsCharsToNum(self):
		self._testBuiltInFunctions('commonChars', 'checkCharsToNum')

	def test_createPreTest(self):
		alph = alphabet()
		en = englishString.small()
		alph.create(en)

		with self.assertRaises(KeyError):
			alph[1000]
		with self.assertRaises(KeyError):
			alph["ad"]

	def test_createNumToChars(self):
		self._testBuiltInFunctions('create', 'checkNumToChars')

	def test_createCharsToNum(self):
		self._testBuiltInFunctions('create', 'checkCharsToNum')
