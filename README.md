## Project name and brief synopsis

**pymetrics** is an exceptionally efficient and simple logging tool for capturing and analysing important system information.

This command line application basically dives into linux logs, captures data, and aggregates them into a single location after analysing them. 
This saves Linux users the time and effort of manually parsing the many log files, which is in itself an inefficient and error-prone process.

pymetrics is a highly configurable logging tool. 
It comes with its own configuration file, written in YAML, which can be modified to change certain behaviours of the application to suit the user's taste. 
Users can even specify a different, custom configuration file which will be consumed by the program. 

A full description of the capabilities of this application will be given under the **features** section.


**Note:** pymetrics was not built with maximum portability in mind. 
However, a great deal of effort was made to make it as portable as possible. 
What this means in practice is that this tool is specially suited to run on Unix-like systems. 
While this program will run on non-linux systems, it is likely to run into some unexpected issues - especially when handling log files.
Also, collection of certain metrics will be omitted. 
This issue can be mitigated though with a little tweaking of the configuration file. 

___This is an ongoing project. Features and capabilities are being added on a continuous basis.___

You are welcome to view the `Contributing.md` file if you wish to contribute to this project.


## Features
1. ##### Cloud Integration
 - pymetrics beutifully integrates with your AWS environment by storing log reports in an S3 bucket.
   - This is an optional feature which can be enabled by modifying the configuration file.
   - This feature will not work correctly unless your AWS environment has been properly configured through the `aws configure` CLI command.
 - pymetrics also fetures a lambda function that notifies you whenever your log files are uploaded to the preconfigued S3 bucket.
   - This lambda function is fully robust and has error-handling capabilities embeded in it. However, you will need to modify it in order to add the arn (Amazon Resource Name) of your SNS Service.
   - You will also need to manually configure the S3 bucket as a trigger for the lambda function.
 - This lambda function is also designed to log its activities to CloudWatch for reference or debugging purposes.
   - Thus appropriate permissions must be granted in the IAM role which the function will have to assume.
    
2. ##### Configuration
 - pymetrics reads from its default configuration file, **pymetrics.conf.yml**. This configuration file is consumed by the program at execution and it defines the behaviour of the program. 
 - **A different configuration file can also be passed to the program by using the `-c` option.**
 - Any configuration file passed to the program must be written in YAML and must closely mirror the default configuration file. 
   - Keys or values not provided in the configuration file are marked as illegal keys/values and the program will refuse to parse them. 
   - This can cause the program execution to fail. 
   - **You can test your configuration file by running the program with the `-t` or `-T` option.**

3. ##### System Information 
 - pymetrics collects other system information like the OS name, OS type, nodename, active interfaces, current IP addresses, user statistics (number of logged in users and their time of login), disk usage information, virtual memory information, cpu statistics, network connectivity information, and so many more. 

4. ##### Log File Analysis 
 - pymetrics searches specified log files and extracts useful information for logging. 
   - By default, pymetrics only analyses a handful of log files. But other log files can be included in the configuration file. 
   - Only the files present in the configuration file can be parsed by the program. 
 - pymetrics also specially analyses Web server logs, if present, and collects useful metrics from them. 

5. ##### Log Access 
 - pymetrics logs a report each time it is executed. 
 - The access log information contains the date, time and user who executed the program. 
This can be useful for auditing purposes. 
This is stored in the *access.log* file. 

6. ##### Log Errors 
 - pymetrics will print a message to the screen if it encounters an exception.
 - Error messages are broadly categorised as *Error* and *Info*. 
   - Error message means the application has encountered an exception which it couldn't handle. 
   - Info message means the application encountered an exception, but was able to gracefully handle it. 
   - Both errors from the *Error* and *Info* categories are logged in the *error.log file.* 
   - This file should be your first port of call when something in the application does not work as expected.
  
 
7. ##### Log Reports
 - Log reports are stored in the logs directory of the projects directory. 
 - By default, logs are stored in plain text. 
   - The configuration file can be edited to store the logs in other file formats.
   - Other accepted file formats are _csv_ and _json_. 
   - **A different log format option can be specified at runtime by using the `-f` or `--format` option.** 

8. ##### Email Reports 
 - If a valid email address is specified in the configuration file, an email report will be sent to the address anytime the program is executed. 
 - Of course, this would only work if a working email server (e.g Postfix) is present on the system. 
   - **An email address can also be provided on the fly (at runtime) by using the `-e` or `--email` option**

9. ##### Garbage collection 
 - pymetrics has a fully functional garbage collection utility built into it. 
 - This utility handles the removal of old logs. 
 - By default, log files older than 7 days are deleted. 
   - This behaviour can be changed by modifying the configuration file. 
 - pymetrics' garbage collection utility also deletes empty log files which might have been created by the application at runtime.

## Installation And Usage 

**To be able to use this application;**
 - clone this repository to your local system (`git clone https://github.com/Kelvinskell/pymetrics.git` or `git clone git@github.com:Kelvinskell/pymetrics.git`). 
 - Switch (`cd`) into the cloned repository (*pymetrics*) and execute the **main.py** file by running either `python3 main.py` or `./main.py` on your terminal.
 - You can further create an alias to simplify things. 
 - Install the necessary modules. You can use `pip install <module>` or any other methods. 
 - The following modules are required:
   - [x] distro
   - [x] humanize
   - [x] netifaces
   - [x] pyYAML
   - [x] requests
   - [x] boto3

**If program execution is successful, no output will be printed to the screen.**


It is my hope that this application will serve your purposes.

Connect with me on [LinkedIn](https://www.linkedin.com/in/kelvin-onuchukwu-3460871a1) 
