#!/usr/bin/env python3

import re
import os
import platform
from datetime import datetime

logdate = datetime.now().strftime('%b %e')
date = datetime.today().strftime('%Y-%m-%d')
filepath = f'report-{date}.txt'

class Logs():
        ########## Garbage collection will remove any empty files ##########
    def __init__(self, values):
        self.values = values

    def logSudo(self):
        # Check file existence and read access
        if "/var/log/sudo.log" in self.values["log_files"]:
            sudo = '/var/log/sudo.log'
        if not os.access(sudo, os.F_OK) or not os.access(sudo, os.R_OK):
            return False

        # Create path
        dirpath = 'logs/sudo'

        # Open file
        if not os.path.isdir(dirpath):
            os.mkdir(dirpath)
        logfile = open(os.path.join(dirpath, filepath), 'w')

        # Log to file
        pattern = r'{}'.format(logdate)
        with open(sudo) as file:
            lines = file.readlines()
            for i in range(0, len(lines)):
                line1 = lines[i]
                if re.search(f'^{pattern}', line1):
                    logfile.write(line1)
                    line2 = lines[i + 1]
                    logfile.write(line2)
        logfile.close()
        return True

    def logCron(self):
        # Check file existence and read access
        if "/var/log/cron.log" in self.values["log_files"]:
            cron = '/var/log/cron.log'
        if not os.access(cron, os.F_OK) or not os.access(cron, os.R_OK):
            return False
        
        # Create path
        dirpath1 = 'logs/cron'
        dirpath2 = 'logs/anacron'

        # Open file
        if not os.path.isdir(dirpath1):
            os.mkdir(dirpath1)
        logfile = open(os.path.join(dirpath1, filepath), 'w')

        # Log to file
        anacronpattern = r"^(Jun  6) ([:\d]+) (.*?)anacron\[\d+\]".format(logdate) 
        cronpattern = r"^({}) ([:\d]+) (.*?)CRON\[\d+\]".format(logdate)
        with open(cron) as file:
            lines = file.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if re.search(f'{cronpattern}', line):
                    logfile.write(line)
        logfile.close()

        if not os.path.isdir(dirpath2):
            os.mkdir(dirpath2)
        logfile = open(os.path.join(dirpath2, filepath), 'w')

        with open(cron) as file:
            lines = file.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if re.search(f'{anacronpattern}', line):
                    logfile.write(line)
        logfile.close()
        return True

    def logAuth(self):
        # Check file existence and read access
        if "/var/log/auth.log" in self.values["log_files"]:
            auth = '/var/log/auth.log'
        if not os.access(auth, os.F_OK) or not os.access(auth, os.R_OK):
            return False

        # Create path
        dirpath = 'logs/auth'

        # Open file
        if not os.path.isdir(dirpath):
            os.mkdir(dirpath)
        logfile = open(os.path.join(dirpath, filepath), 'w')

        authpattern = r"^(Jun  6) ([:\d]+) (.*?)(sshd|systemd-logind)\[\d+\]".format(logdate) 

        with open(auth) as file:
            lines = file.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if re.search(f'{authpattern}', line):
                    logfile.write(line)
        logfile.close()
        return True
