## Project name and brief synopsis

**pymetrics** is an exceptionally efficient and simple logging tool for capturing and analysing important system information.

This program basically dives into linux logs, captures data, and aggregates them into a single location after analysing them. 
This saves Linux users the time and effort of manually parsing the many log files, which is in itself an inefficient and error-prone process.

pymetrics is a highly configurable logging tool. 
It comes with its own configuration file, written in YAML, which can be modified to change certain behaviours of the program to suit the user's taste. 
Users can even specify a different, custom configuration file which will be consumed by the script. 

A full description of the capabilities of this script will be given under the **features** section.

**Note:** pymetrics was not built with portability in mind. 
What this means in practice is that this tool is specially suited to run on Unix-like systems. 
While this script will run on non-linux systems, it is likely to run into some unexpected issues - especially when handling log files. 
This issue can be mitigated though with a little tweaking of the configuration file. 

___This is an ongoing project. Features and capabilities are being added on a continuous basis.___

You are welcome to view the `Contributing.md` file if you wish to contribute to this project.

You can also reach me directly on [LinkedIn](www.linkedin.com/in/kelvin-onuchukwu-3460871a1) 

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
 - The access log information contains the date, time and user who executed the script. This can be useful for auditing purposes. 
 
5. ##### Log Reports
 - Log reports are stored in the logs directory of the projects directory. 
 - By default, logs are stored in plain text. 
   - The configuration file can be edited to store the logs in other file formats.
   - Other accepted file formats are _csv_ and _json_. 
   - **A different log format option can be specified at runtime by using the `-f` or `--format` option.** 

6. ##### Email Reports 
 - If a valid email address is specified in the configuration file, an email report will be sent to the address whenever the script is executed. 
 - Of course, this would only work if a working email server (Postfix) is present on the system. 
   - **An email address can also be provided on the fly (at runtime) by using the `-e` or `--email` option**
