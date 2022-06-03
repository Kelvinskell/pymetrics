#!/usr/bin/env python3

import re
import os
from datetime import timedelta

class DeleteLog():
    def __init__(self, values):
        self.values = values

    def extractDate(self):
        nested_list = []
        file_dates = []
        pattern = r"([_a-zA-Z]+)-([\d-]+)(\.txt|\.csv|\.json)$"
        if os.path.isdir('logs'):
            for parentdir, subdir, namelists in os.walk("logs"):
                nested_list.append(namelists)
            # Extract each filename from list of filenames
            flattened_list = [file for sublist in nested_list for file in sublist]

            for filename in flattened_list:
                regex = re.search(pattern, filename)
                if regex:
                    file_dates.append(regex.group(2))
            self.filedates = file_dates
            return self.filedates

