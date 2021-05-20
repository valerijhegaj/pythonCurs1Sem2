import unittest
import sys
import os
sys.path.append(os.path.join(sys.path[0], "../src/"))

from test import EnglishTest
from test import DictingTest
from test import AlphabetTest
from test import CaesarCipherTest 	#works for about 0.2с
from test import InteractionTest
from test import VegenerCipherTest
from test import VernamTest
from test import InterfaceTest
from test import ParserTest
from test import WebTest 			#works for about 2с-3c
#other tests is quick

unittest.main()