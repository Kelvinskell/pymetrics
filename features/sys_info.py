#!/usr/bin/env python3

# Import modules
try:
    import csv
    import distro
    import json
    import netifaces
    import os
    #import psutil
    import platform
    import re
    import requests
    import socket
    import sys
    from datetime import datetime
    from datetime import date
except ModuleNotFoundError as error:
    print(f"pymetrics: Error: {error}. \nUse 'pip install' to install module.")

class SysFetch():
    # Initialise values
    def __init__(self, values):
        try:
            self.architecture = platform.machine()
            #self.boot_time = datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
            #self.cpu_cores = psutil.cpu_count()
            self.distro = distro.id()
            self.nodename = socket.gethostname()
            self.os_type = platform.system()
            self.user = os.getlogin()
            self.version = platform.release()
            self.date = date.today()
            self.time = datetime.now().strftime("%H:%M:%S")
            self.values = values
            self.interfaces = netifaces.interfaces()
        except PermissionError as error:
            print("pymetrics: Error: Not enough permissions.")

    def generalInfo(self):
        info = {}
        info["architecture"] = self.architecture
        info["boot"] = "self.boot_time"
        info["cpu_cores"] = "self.cpu_cores"
        info["distribution"] = self.distro 
        info["nodename"] = self.nodename
        info["os_type"] = self.os_type
        info["version"] = self.version
        if not all(info.values()):
            print("pymetrics: Info: Unable to collect some metrics.")
        self.info = info
        return self.info


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

# Log collected system metrics
class LogSysFetch(SysFetch):
    def __init__(self, values):
        self.values = values
        SysFetch.__init__(self, values)

    def logGeneral(self):
        report = SysFetch.generalInfo(self)
        if not os.path.isdir("logs/system_info"):
            try:
                os.makedirs("logs/system_info")
            except PermissionError:
                print("pymetrics: Error: Unable to log reports. \nNot enough permissions.")

        # Read config file
        log_format = self.values["log_format"]

        # Log in plain text
        if log_format == "plain_text":
            with open(f"logs/system_info/report-{self.date}.txt", "w") as file:
                for key, value in self.info.items():
                    file.write("{} -----------> {}\n".format(key, value))
        

