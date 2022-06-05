#!/usr/bin/env python3

# Import modules
try:
    import os
    import socket
    import platform
    from datetime import datetime
    from datetime import date
except ModuleNotFoundError as error:
    print(f"pymetrics: Error: {error}. \nUse 'pip install' to install module")

# Log a report whenever main.py is executed
class WriteToErrorLog():
    def __init__(self, message):
        # Collect system information
        self.system_type = platform.system()
        self.user = os.getlogin()
        self.nodename = socket.gethostname()
        self.date = date.today()
        self.time = datetime.now().strftime("%H:%M:%S")
        self.message = message

    def log(self):
        if not os.path.isdir("logs"):
            os.mkdir("logs")
        with open("logs/error.log", "a") as file:
            file.write(f"{self.date} {self.time} {self.system_type} {self.nodename} {self.user} {self.message}\n")
        return

