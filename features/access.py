#!/usr/bin/env python3

# Import modules
try:
    import os
    import pwd
    import socket
    import platform
    from datetime import datetime
    from datetime import date
except ModuleNotFoundError as error:
    print(f"pymetrics: Error: {error}. \nUse 'pip install' to install module")

# Log a report whenever main.py is executed
class WriteToAccessLog():
    def __init__(self):
        # Collect system information
        self.system_type = platform.system()
        # self.user = os.getlogin()
        self.user = pwd.getpwuid(os.geteuid())[0]
        self.nodename = socket.gethostname()
        self.date = date.today()
        self.time = datetime.now().strftime("%H:%M:%S")

    def log(self):
        if not os.path.isdir("logs"):
            os.mkdir("logs")
        with open("logs/access.log", "a") as file:
            file.write(f"pymetrics: {self.date} {self.time} {self.system_type} {self.nodename} {self.user}\n")
        return

