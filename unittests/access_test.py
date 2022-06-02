#!/usr/bin/env python3

import unittest
import sys

# Import modules for testing
sys.path.append('../features')
from access import WriteToAccessLog

# Instantiate class
access_class = WriteToAccessLog()

class TestAccessWrite(unittest.TestCase):
    def test_log(self):
        self.assertIsNone(access_class.log())

unittest.main()
