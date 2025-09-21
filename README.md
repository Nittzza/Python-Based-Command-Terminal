# Simple Python Terminal

A lightweight Python-based command terminal with ASCII art and essential features.

## Features

✅ **ASCII Art Banner** - Beautiful terminal startup display  
✅ **File Operations** - ls, cd, pwd, mkdir, rm, cat  
✅ **System Monitoring** - CPU, memory, disk usage, process list  
✅ **Error Handling** - Graceful error messages  
✅ **System Commands** - Execute any system command  
✅ **Clean Interface** - Simple and responsive CLI

## Quick Start

1. Install dependencies:

```bash
pip install psutil
```

2. Run the terminal:

```bash
python simple_terminal.py
```

## Available Commands

- `help` - Show available commands
- `exit/quit` - Exit the terminal
- `pwd` - Print working directory
- `ls` - List directory contents
- `cd <dir>` - Change directory
- `mkdir <name>` - Create directory
- `rm <file>` - Remove file
- `cat <file>` - Display file contents
- `echo <text>` - Print text
- `clear` - Clear screen
- `sysinfo` - Show system information
- `ps` - List running processes
- `<command>` - Execute any system command

## Example Usage

```
terminal@Documents: /Users/user/Documents$ ls
📁 projects/
📄 notes.txt
📄 README.md

terminal@Documents: /Users/user/Documents$ mkdir test
Created directory: test

terminal@Documents: /Users/user/Documents$ sysinfo
🖥️  System Information:
   CPU Usage: 15.2%
   Memory: 45.3% used (7GB / 16GB)
   Disk: 23.1% used (120GB / 500GB)
   Platform: darwin
```

## Requirements

- Python 3.6+
- psutil (for system monitoring)
# Python-Based-Command-Terminal
