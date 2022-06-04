#!/usr/bin/env python3

import sys
# Import unittest library
import unittest

# Import module for testing
sys.path.append('../features')
import config_parse

# Instantiate YamlParser class
parse_class = config_parse.YamlParser('../pymetrics.conf.yml')

class TestYamlParser(unittest.TestCase):
    def test_basic(self):
        self.assertTrue(parse_class.yaml_to_python())

unittest.main()
