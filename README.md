## Project name and brief synopsis

**pymetrics** is an exceptionally efficient and simple logging tool for capturing and analysing important system information.

This program basically dives into linux logs, captures data, and aggregates them into a single location after analysing them. 
This saves Linux users the time and effort of manually parsing the many log files, which is in itself an inefficient and error-prone process.

pymetrics is a highly configurable logging tool. 
It comes with its own configuration file, written in YAML, which can be modified to change certain behaviours of the program to suit the user's taste. 
Users can even specify a different, custom configuration file which will be consumed by the script. 

A full description of the capabilities of this script will be given under the **features** section.

**Note:** pymetrics was not built with maximum portability in mind. 
However, a great deal of effort was made to make it as portable as possible. 
What this means in practice is that this tool is specially suited to run on Unix-like systems. 
While this script will run on non-linux systems, it is likely to run into some unexpected issues - especially when handling log files.
Also, collection of certain metrics will be omitted. 
This issue can be mitigated though with a little tweaking of the configuration file. 

___This is an ongoing project. Features and capabilities are being added on a continuous basis.___

You are welcome to view the `Contributing.md` file if you wish to contribute to this project.


## Features

1. ##### Configuration
 - pymetrics reads from its default configuration file, **pymetrics.conf.yml**. This configuration file is consumed by the script at execution and it defines the behaviour of the script. 
 - **A different configuration file can also be passed to the script by using the `-c` option.**
 - Any configuration file passed to the script must be written in YAML and must closely mirror the default configuration file. 
   - Keys or values not provided in the configuration file are marked as illegal keys/values and the script will refuse to parse them. 
   - This can cause the program execution to fail. 
   - **You can test your configuration file by running the script with the `-t` or `-T` option.**

2. ##### System Information 
 - pymetrics collects other system information like the OS name, OS type, nodename, active interfaces, current IP addresses, user statistics (number of logged in users and their time of login), disk usage information, virtual memory information, cpu statistics, network connectivity information, and so many more. 

3. ##### Log File Analysis 
 - pymetrics searches specified log files and extracts useful information for logging. 
   - By default, pymetrics only analyses a handful of log files. But other log files can be included in the configuration file. 
   - Only the files present in the configuration file can be parsed by the script. 
 - pymetrics also specially analyses Web server logs, if present, and collects useful metrics from them. 

4. ##### Log Access 
 - pymetrics logs a report each time it is executed. 
 - The access log information contains the date, time and user who executed the script. 
This can be useful for auditing purposes. 
This is stored in the *access.log* file. 

5. ##### Log Errors 
 - pymetrics will print a message to the screen if it encounters an exception.
 - Error messages are broadly categorised as *Error* and *Info*. 
   - Error message means the program has encountered an exception which it couldn't handle. 
   - Info message means the program encountered an exception, but was able to gracefully handle it. 
   - Both errors from the *Error* and *Info* categories are logged in the *error.log file.* 
  
 
6. ##### Log Reports
 - Log reports are stored in the logs directory of the projects directory. 
 - By default, logs are stored in plain text. 
   - The configuration file can be edited to store the logs in other file formats.
   - Other accepted file formats are _csv_ and _json_. 
   - **A different log format option can be specified at runtime by using the `-f` or `--format` option.** 

7. ##### Email Reports 
 - If a valid email address is specified in the configuration file, an email report will be sent to the address whenever the script is executed. 
 - Of course, this would only work if a working email server (e.g Postfix) is present on the system. 
   - **An email address can also be provided on the fly (at runtime) by using the `-e` or `--email` option**

8. ##### Garbage collection 
 - pymetrics has a fully functional garbage collection utility built into it. 
 - This utility handles the removal of old logs. 
 - By default, log files older than 7 days are deleted. 
   - This behaviour can be changed by modifying the configuration file. 

## Installation And Usage 

**To be able to use this program;**
 - clone this repository to your local system (`git clone https://github.com/Kelvinskell/pymetrics.git` or `git clone git@github.com:Kelvinskell/pymetrics.git`). 
 - Switch (`cd`) into the cloned repository (*pymetrics*) and execute the **main.py** file by running either `python3 main.py` or `./main.py` on your terminal.
 - You can further create an alias to simplify things. 
 - Install the necessary modules. You can use `pip install <module>` or any other methods. 
 - The following modules are required:
   - [x] argparse
   - [x] distro
   - [x] humanize
   - [x] netifaces
   - [x] pyyaml
   - [x] requests

**If program execution is successful, no output will be printed to the screen.**


It is my hope that this program will serve your purposes.

Connect with me on [LinkedIn](https://www.linkedin.com/in/kelvin-onuchukwu-3460871a1) 
