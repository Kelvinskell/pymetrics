#!/usr/bin/env python3

import argparse
from features import config_parse

parser = config_parse.YamlParser("default.conf.yml")
parsed_values = parser.yaml_to_python()
