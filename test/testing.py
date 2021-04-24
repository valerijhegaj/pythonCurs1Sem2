import unittest
import sys
import os
sys.path.append(os.path.join(sys.path[0], "../src/"))
from test import englishTest
from test import dictingTest
from test import alphabetTest
from test import CaesarCipherTest
from test import interactionTest
from test import VegenerCipherTest
from test import VernamTest

unittest.main()