#!/usr/bin/env python3

# Import testing library
import unittest

# Import module to be tested
import sys
sys.path.append('../features')
import sys_info

values = {"log_format": "plain_text", "url": "https://google.com", "timeout" : 4}

# Instantiate class
testunit = sys_info.SysFetch(values)

class TestSysFetch(unittest.TestCase):
    def testConnection(self):
        self.assertTrue(testunit.check_connectivity())

    def testLog(self):
        self.assertIsNone(sys_info.plainLog(fp="testfile", values=values.items()))


unittest.main()

