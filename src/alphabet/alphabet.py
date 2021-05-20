from alphabet.dicting          import Dicting
from alphabet.english          import EnglishString
from alphabet.frequencyEnglish import FrequencyEnglish

class Alphabet(dict):
    frequency = None

    def copy_dict(self, dictionary):
        self.clear()
        for i in dictionary:
            self[i] = dictionary[i]

    def create(self, alph, freq = None):
        self.copy_dict(Dicting.create(alph))
        self.frequency = freq

    def create_small(self):
        self.create(EnglishString.small(), FrequencyEnglish.get_frequency())

    def create_small_and_big(self):
        self.create(EnglishString.small_and_big())

    def create_common_chars(self):
        self.create(EnglishString.common_chars())

    def get_frequency(self):
        return self.frequency
