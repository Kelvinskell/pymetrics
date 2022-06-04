#!/usr/bin/env python3

import unittest
import sys

# Import modules for testing
sys.path.append('..')
from main import logAccess
from main import logMetrics

class TestAccess(unittest.TestCase):
    def test_bool(self):
        testcase = bool(logAccess())
        expected = True
        self.assertEqual(testcase, expected)

    def test_none(self):
        self.assertIsNotNone(logAccess())

class TestMetrics(unittest.TestCase):
    def test_bool(self):
        testcase = bool(logMetrics())
        expected = True
        self.assertEqual(testcase, expected)

    def test_none(self):
        self.assertIsNotNone(logMetrics())

unittest.main()
