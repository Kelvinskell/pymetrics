#!/usr/bin/env python3

# Import modules
try:
    import csv
    import distro
    import humanize
    import json
    import netifaces
    import os
    import psutil
    import platform
    import re
    import requests
    import socket
    import shutil
    import subprocess
    import sys
    from datetime import datetime
    from datetime import date
except ModuleNotFoundError as error:
    print(f"pymetrics: Error: {error}. \nUse 'pip install' to install module.")

# Plain text log formatting 
# fp means file pointer
def plainLog(fp, values, mode="w"):
            # Create a new file if file doesnt exist append if it exists
            # For login_info directory
            if re.search("logs/login_info", fp):
                if os.path.isfile(fp):
                    mode = "a"
                else:
                    mode = "w"

            with open(fp, mode) as txt_file:
                for key, value in values:
                    txt_file.write("{} -----------> {}\n".format(key, value))

# Csv log formatting
def csvLog(fp, value_items, value_keys):
            log = [value_items]
            keys = [key for key in value_keys]
            with open(fp, "w") as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=keys)
                writer.writeheader()
                writer.writerows(value_items)

# json log formatting
def jsonLog(fp, values, mode="w"):

            # Create a new file if file doesnt exist append if it exists
            # For connection_info and login_info directory
            if re.search(r"logs/(connection_info|login_info)", fp):
                if os.path.isfile(fp):
                    mode = "a"
                else:
                    mode = "w"

            with open(fp, mode) as json_file:
                json.dump(values, json_file,  indent=6, separators=(' , ', ' : '), sort_keys=True)


class SysFetch():
    # Initialise values
    def __init__(self, values):
        try:
            self.architecture = platform.machine()
            self.boot_time = datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
            self.cpu_cores = psutil.cpu_count()
            self.distro = distro.id()
            self.nodename = socket.gethostname()
            self.os_type = platform.system()
            self.user = os.getlogin()
            self.version = platform.release()
            self.date = date.today()
            self.time = datetime.now().strftime("%H:%M:%S")
            self.total_disk = shutil.disk_usage('/').total
            self.free_disk = shutil.disk_usage('/').free
            self.used_disk = shutil.disk_usage('/').used
            self.total_virt = psutil.virtual_memory().total
            self.free_virt = psutil.virtual_memory().free
            self.used_virt = psutil.virtual_memory().used
            self.values = values
            self.interfaces = netifaces.interfaces()
        except PermissionError as error:
            print("pymetrics: Error: Not enough permissions.")

    def generalInfo(self):
        info = {}
        info["architecture"] = self.architecture
        info["boot"] = self.boot_time
        info["cpu_cores"] = self.cpu_cores
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
            if request.status_code == 200:
                self.request = True
                return self.request
        except (requests.ConnectionError, requests.Timeout):
            self.request = False
            return self.request

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
        self.interface_names = interface_names
        self.ip_addresses = ip_addresses
        return self.interface_names, self.ip_addresses

    def check_mem(self):
        free_disk = humanize.naturalsize(self.free_disk)
        total_disk = humanize.naturalsize(self.total_disk)
        used_disk = humanize.naturalsize(self.used_disk)
        free_virt = humanize.naturalsize(self.free_virt)
        total_virt = humanize.naturalsize(self.total_virt)
        used_virt = humanize.naturalsize(self.used_virt)
        percent_diskused = self.used_disk / self.total_disk * 100
        percent_diskfree = self.free_disk / self.total_disk * 100
        percent_virtused = self.used_virt / self.total_virt * 100
        percent_virtfree = self.free_virt / self.total_virt * 100
        
        # Round off percent to 2 decimal places
        percent_diskused = "{:.2f}".format(percent_diskused)
        percent_diskfree = "{:.2f}".format(percent_diskfree)
        percent_virtused = "{:.2f}".format(percent_virtused)
        percent_virtfree = "{:.2f}".format(percent_virtfree)

        disk_values = {"free disk": free_disk, 
                "total disk": total_disk, 
                "used_disk": used_disk,
                "free virt mem": free_virt,
                "total virt mem": total_virt,
                "used virt mem": used_virt,
                "percentage free disk": "{}%".format(percent_diskfree),
                "percentage used disk": "{}%".format(percent_diskused),
                "percent free virt mem": "{}%".format(percent_virtfree),
                "percent used virt mem": "{}%".format(percent_virtused)
                }
        self.disk_values = disk_values
        return self.disk_values

    def check_login(self):
        # Run only on linux systems
        if platform.system() == 'Linux':
            users = subprocess.check_output('who').decode('utf-8')
            usernames = [x.split()[0] for x in users.splitlines()]
            logins = [x.split()[3] for x in users.splitlines()]
            self.usernames = usernames
            self.logins = logins
            login_values = dict(zip(self.usernames, self.logins))
            self.login_values = login_values
            return self.login_values


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

        # Read config info
        log_format = self.values["log_format"]

        # Log in plain text
        if log_format == "plain_text":
            plainLog(fp=f"logs/system_info/report-{self.date}.txt", values=self.info.items())

        # Log in csv format
        if log_format == "csv":
            csvLog(fp=f"logs/system_info/report-{self.date}.csv", value_items=[dict(self.info.items())], value_keys=self.info.keys())

        # Log in json format
        if log_format == "json":
            jsonLog(fp=f"logs/system_info/report-{self.date}.json",values=dict(self.info.items()))

    def logConnection(self): 
        report = SysFetch.check_connectivity(self)
        # Read config info
        log_format = self.values["log_format"]

        if not os.path.exists("logs/connection_info"):
            os.mkdir("logs/connection_info")

        # Log in plain text
        if log_format == "plain_text":
            log_file = f"logs/connection_info/report-{self.date}.txt"
            
             #Create a new file if file doesnt exist append if it exists
            if os.path.isfile(log_file):
                mode = "a"
            else:
                mode = "w"

            with open(log_file, mode) as text_file:
                    if self.request:
                        text_file.write("{}: Internet Connection ----------> Active\n".format(self.time))
                    else:
                        text_file.write("{}: Internet Connection ----------> Not Active\n".format(self.time))
        # Log in json format
        if log_format == "json":
            log_file = f"logs/connection_info/report-{self.date}.json"
            connection_values = {"time": self.time, "internet": self.request}  
            jsonLog(fp=log_file, values=connection_values)

    def logInterface(self):
        report = SysFetch.check_interfaces(self)

        # Read config value
        log_format = self.values["log_format"]

        dirpath = "logs/interface_info"
        if not os.path.isdir(dirpath):
            os.mkdir(dirpath)

        # Create a dictionary of interface names to IP addresses
        ip_dict = dict(zip(self.interface_names, self.ip_addresses))
        
        # Log plain text
        if log_format == "plain_text":
            log_file = os.path.join(dirpath, f"report-{self.date}.txt")
            plainLog(fp=log_file, values=ip_dict.items())

        # Log csv
        if log_format == "csv":
            log_file = os.path.join(dirpath, f"report-{self.date}.csv")

            csvLog(fp=log_file, value_items=[dict(ip_dict.items())], value_keys=ip_dict.keys())

        # Log json
        if log_format == "json":
            log_file = os.path.join(dirpath, f"report-{self.date}.json")
            jsonLog(fp=log_file, values=dict(ip_dict.items()))


    def logMem(self):
        report = SysFetch.check_mem(self)

        # Read config file
        log_format = self.values["log_format"]

        dirpath = "logs/mem_info"
        if not os.path.isdir(dirpath):
            os.mkdir(dirpath)

        values = self.disk_values

        # Log plain text
        if log_format == "plain_text":
            log_file = os.path.join(dirpath, f"report-{self.date}.txt")
            plainLog(fp=log_file, values=values.items())


        # Log csv
        if log_format == "csv":
            log_file = os.path.join(dirpath, f"report-{self.date}.csv")
            csvLog(fp=log_file, value_items=[dict(values.items())], value_keys=values.keys())

        # log json
        if log_format == "json":
            log_file = os.path.join(dirpath, f"report-{self.date}.json")
            jsonLog(fp=log_file, values=dict(values.items()))

    def logLogin(self):
        report = SysFetch.check_login(self)
        if report:

            # Read config file
            log_format = self.values["log_format"]

            dirpath = "logs/login_info"
            if not os.path.isdir(dirpath):
                os.mkdir(dirpath)

            values = self.login_values

            #Log plain text
            if log_format == "plain_text":
                log_file = os.path.join(dirpath, f"report-{self.date}.txt")
                plainLog(fp=log_file, values=values.items())

                # Log json
                if log_format =="json":
                    log_file = os.path.join(dirpath, f"report-{self.date}.json")
                    jsonLog(fp=log_file, values=dict(values.items()))
