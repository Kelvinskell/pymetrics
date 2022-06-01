#!/usr/bin/env python3

import sys
import yaml
from yaml import scanner
from yaml import parser
import json

class YamlParser():
    def __init__(self, yaml_file):
        self.yaml_file = yaml_file

    # Convert yaml to python object
    def yaml_to_python(self):
        with open(self.yaml_file) as file:
            try:
                configuration = yaml.safe_load(file)
            except (scanner.ScannerError, parser.ParserError):
                print("pymetrics: Error: Unable to parse YAML. \nMalformed configuration file.")
                return False
            except:
                print("pymetrics: Error: Cowardly refusing to parse file. \nUnkown Error detected")
                return False
            if not bool(configuration):
                print("pymetrics: Error: Empty or damaged configuration file")
                return False
            return configuration
