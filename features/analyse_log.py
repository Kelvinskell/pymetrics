#!/usr/bin/env python3

import re
import os
from datetime import datetime

logdate = datetime.now().strftime('%b %e')
date = datetime.today().strftime('%Y-%m-%d')
time = datetime.today().strftime('%H:%M:%S')

class Logs():
    def __init__(self, values):
        self.values = values

    def logSudo(self):
        # Check file existence and read access
        for file in self.values["log_files"]:
            if file == "/var/log/sudo.log":
                sudo = file
        if os.access(sudo, os.F_OK) and os.access(sudo, os.R_OK):

            # Create path
            dirpath = 'logs/sudo'
            filepath = f'report-{date}.txt'

            # Open file
            if not os.path.isdir(dirpath):
                os.mkdir(dirpath)
            logfile = open(os.path.join(dirpath, filepath), 'w')

            # Log to file
            pattern = r'{}'.format(logdate)
            with open('sudo.log') as file:
                lines = file.readlines()
                for i in range(0, len(lines)):
                    line1 = lines[i]
                    if re.search(f'^{pattern}', line1):
                        logfile.write(line1)
                        line2 = lines[i + 1]
                        logfile.write(line2)
            logfile.close()
            ########## Garbage collection will remove empty files ##########
   


