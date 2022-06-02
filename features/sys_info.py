#!/usr/bin/env python3

# Import modules
import distro
import netifaces
import os
import psutil
import platform
import re
import requests
import socket
from datetime import datetime
from datetime import date

class SysFetch():
    # Initialise values
    def __init__(self, values):
        self.boot_time = datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
        self.cpu_cores = psutil.cpu_count()
        self.distro = distro.id()
        self.nodename = socket.gethostname()
        self.os_type = platform.system()
        self.user = os.getlogin()
        self.version = platform.release()
        self.date = date.today()
        self.time = datetime.now().strftime("%H:%M:%S")
        self.values = values
        self.interfaces = netifaces.interfaces()

    def check_connectivity(self):
        # Test network conectivity
        self.url = self.values["url"]
        self.timeout = self.values["timeout"]
        try:
            request = requests.get(self.url, timeout=self.timeout)
            return request.status_code == 200
        except (requests.ConnectionError, requests.Timeout):
            return False

    def check_interfaces(self):
        '''Test for active network interfaces and extract the IP addresses associated with them.
        Return active interface names and Ip addresses as a tuple of two seperate lists.'''
        interface_names = []
        ip_addresses = []
        for interface in self.interfaces:
            addr = netifaces.ifaddresses(interface)
            for key, value in addr.items():
                string_value = str(value)
                regex = re.findall(r"'addr': ['\.\d]+(?=[, 'netmask']+)", string_value)
                if regex:
                    string_regex = str(regex)
                    ip_addr = string_regex.split()[-1].strip("']\"")
                    interface_names.append(interface)
                    ip_addresses.append(ip_addr)
        return interface_names, ip_addresses

