#!/usr/bin/env python3

import re
import os
from datetime import timedelta
from datetime import datetime
from datetime import date

class DeleteLog():
    def __init__(self, values):
        self.values = values

        # Make filedate avilable to other functions within this class
        self.extractDate()
        self.formatDate()

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
            return self.file_dates

    def formatDate(self):
        date_format = "%Y-%m-%d"
        date_range = []

        # Read config value
        expire_after = self.values["expire_logs"]

        # Get today's date
        current_date = str(datetime.today().strftime("%Y-%m-%d"))
        current_date = datetime.strptime(current_date, date_format)

        # Add one to value of current date, to prevent false values
        current_date = current_date + timedelta(1)

        # Get dates between today's date and 'expire_after'
        for date in range(expire_after):
            formatted_date = current_date - timedelta(date)
            date_range.append(formatted_date)
        
        # Format file_dates using a generator expression 
        if self.file_dates:
            extracted_dates = (datetime.strptime(date, date_format) for date in self.file_dates)
            self.date_range = date_range
            self.extracted_dates = extracted_dates
            return self.date_range, self.extracted_dates

    def deleteOldLogs(self):
        old_dates = []
        try:
            # Handle exceptions for incorrect dates that cannot be parsed by strptime
            for date in self.extracted_dates:
                if date not in self.date_range:
                    old_dates.append(str(date).split()[0])
        except ValueError:
            pass

        # Recurse through the directory and extract filenames
        nested_list = []
        for walk in os.walk("logs"):
            for parentdir, subdir, namelists in os.walk("logs"):
                nested_list.append(namelists)

                # Extract each filename from list of filenames
                flattened_list = [file for sublist in nested_list for file in sublist]

                # Search for files containing old dates
                for date in old_dates:
                    for filename in flattened_list:
                        if re.search(date, filename):
                            pathname = os.path.join(parentdir, filename)
                            if os.path.exists(pathname):
                                os.remove(pathname)

                        # Delete empty log files
                        pathname = os.path.join(parentdir, filename)
                        if os.path.exists(pathname):
                            if os.stat(pathname).st_size == 0:
                                os.remove(pathname)
