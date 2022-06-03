#!/usr/bin/env python3

import re
import os
from datetime import timedelta
from datetime import datetime

class DeleteLog():
    def __init__(self, values):
        self.values = values

        # Make filedate avilable to other functions within this class
        self.extractDate()

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
            self.file_dates = file_dates
            #print(self.filedates)
            return self.file_dates

    def formatDate(self):
        # Read config value
        expire_after = self.values["expire_logs"]

        # Format dates
        date_range = []
        date_format = "%Y-%m-%d"
        formatted_dates = [datetime.strptime(date, date_format) for date in self.file_dates]

        for num in range(1, expire_after + 1):
            date_range.append(timedelta(num))
