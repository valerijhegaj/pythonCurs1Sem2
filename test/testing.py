import unittest
import sys
import os
sys.path.append(os.path.join(sys.path[0], "../src/"))

from test import EnglishTest
from test import DictingTest
from test import AlphabetTest
from test import CaesarCipherTest
from test import InteractionTest
from test import VegenerCipherTest
from test import VernamTest
from test import InterfaceTest

unittest.main()