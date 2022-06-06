#!/usr/bin/env python3

import re
import os
from datetime import datetime
logdate = datetime.now().strftime('%b %e')
files = ['sudo.log', 'cron.log', 'auth.log', 'mail.err.1']
date = datetime.today().strftime('%Y-%m-%d')
time = datetime.today().strftime('%H:%M:%S')

def logSudo(values):
    # read config file
    log_format = values['log_format']

    # Create path
    if log_format == 'plain_text':
        ext = '.txt'
    elif log_format == 'csv':
        ext = '.csv'
    else:
        log_format == '.json'
    dirpath = 'logs/sudo'
    filepath = f'report-{date}{ext}'

    # Open file
    if not os.path.isdir(dirpath):
        os.mkdir(dirpath)
    logfile = open(os.path.join(dirpath, filepath), 'w')
    
    # Log to file
    pattern = r'{}'.format(logdate)
    with open('sudo.log') as file:
        lines = file.readlines()
        print(pattern)
        for i in range(0, len(lines)):
            line1 = lines[i]
            if re.search(f'^{pattern}', line1):
                logfile.write(line1)
                line2 = lines[i + 1]
                logfile.write(line2)
    logfile.close()


