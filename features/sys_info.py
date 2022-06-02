#!/usr/bin/env python3

# Import modules
import os
import psutil
import socket
import platform
import distro
import interfaces
from datetime import datetime
from datetime import date

class SysFetch():
    def __init__(self, values):
        self.boot_time = datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
        self.cpu_cores = psutil.cpu_count()
        self.distro = distro.id()
        self.nodename = socket.gethostname()
        self.os_type = platform.system()
        self.user = os.getlogin()
        self.version = platform.release()
        self.date = date.today()
        self.time = datetime.now().strftime(%H:%M:%S)
        self.values = values
        self.interfaces = netifaces.interfaces()
