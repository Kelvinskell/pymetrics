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

__This is an ongoing project. Features and capabilities are being added on a continuous basis.__

You are welcome to view the `Contributing.md` file if you wish to contribute to this project.
