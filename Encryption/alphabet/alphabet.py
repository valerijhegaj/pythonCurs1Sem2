from alphabet.dicting          import dicting
from alphabet.english          import englishString
from alphabet.frequencyEnglish import frequencyEnglish

class alphabet(dict):
    frequency = None

    def _copyDict(self, dictionary):
        self.clear()
        for i in dictionary:
            self[i] = dictionary[i]


    def create(self, alph, freq = None):
        self._copyDict(dicting.create(alph))
        self.frequency = freq

    def createSmall(self):
        self.create(englishString.small(), frequencyEnglish.getFrequency())

    def createSmallAndBig(self):
        self.create(englishString.smallAndBig())

    def createCommonChars(self):
        self.create(englishString.commonChars())

    def getFrequency(self):
        return frequency
