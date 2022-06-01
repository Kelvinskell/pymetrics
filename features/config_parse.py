#!/usr/bin/env python3

import yaml
from yaml import scanner
from yaml import parser
import json

class YamlParser():
    def __init__(self, yaml_file):
        self.yaml_file = yaml_file

    def yaml_to_python(self):
        with open(self.yaml_file) as file:
            try:
                configuration = yaml.safe_load(file)
            except (scanner.ScannerError, parser.ParserError):
                return "pymetrics: Error: Unable to parse YAML. \nMalformed configuration file."
            return configuration

ex = YamlParser("ex.yml")
print(ex.yaml_to_python())
dic = ex.yaml_to_python()
