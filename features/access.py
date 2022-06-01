#!/usr/bin/env python3

# Import modules
import os
import socket
import platform
from datetime import datetime
from datetime import date

# Log a report whenever main.py is executed
class WriteToAccessLog():
    def __init__(self):
        # Collect system information
        self.system_type = platform.system()
        self.user = os.getlogin()
        self.nodename = socket.gethostname()
        self.date = date.today()
        self.time = datetime.now().strftime("%H:%M:%S")

    def log(self):
        if not os.path.isdir("logs"):
            os.mkdir("logs")
        with open("logs/access.log", "a") as file:
            file.write(f"{self.date} {self.time} {self.system_type} {self.nodename} {self.user}\n")
        return

