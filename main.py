#!/usr/bin/env python3

# Import modules
import argparse
import os
import sys
from features import config_parse

# Log usage to logs/access.log
from features import access
access.WriteToAccessLog().log()

# Create the parser
parser = argparse.ArgumentParser(prog="pymetrics", description="Collect, analyse and report useful system meyrics", allow_abbrev=False, epilog="Enjoy the program!")

# Version
parser.version = 'pymetrics: version 1.0'

# Add the arguments
parser.add_argument('-c', metavar='Config_file', action="store", type=str, help="specify alternative yaml configiration file")
parser.add_argument('-t', '--test', action="store_true", help="test configuration and exit")
parser.add_argument('-T', action='store_true', help="test configuration file, dump it and exit")
parser.add_argument('-v', '--version', action='version', help='Print version and exit')

# Execute parse_args method
args = parser.parse_args()

# Define yaml configuration file
if args.c:
    c = args.c
    if not os.path.exists(c):
        print("pymetrics: Error: No such file or directory.")
        sys.exit(1)
    if not os.path.isfile(c):
        print(f"pymetrics: Error: {c} is not a file")
        sys.exit(1)
    config_file = c
else:
    config_file = "pymetrics.conf.yml"

# Read configuration file
parser_class = config_parse.YamlParser(config_file)
parsed_values = parser_class.yaml_to_python()

# Print configuration
if args.test or args.T:
    if parsed_values:
        print(f"The configuration file {config_file} syntax is ok.", end="\n\n")
        if args.T:
            print(parsed_values)
        sys.exit()
    else:
        print(f"The configuration file {config_file} has bad syntax")
        sys.exit(1)

# Load parsed values
log_files = parsed_values["log_files"]
log_format = parsed_values["log_report_format"]
delete_logs = parsed_values["delete_logs"]
expire_logs = parsed_values["expire_logs"]
notify = parsed_values["notify"]
email_address = parsed_values["email_address"]
alert = parsed_values["alert"]
web_log = parsed_values["web_server"]["logs"]
web_data = parsed_values["web_server"]["data"]
values = [log_files, log_format, delete_logs, expire_logs, notify, email_address, alert, web_log, web_data]
