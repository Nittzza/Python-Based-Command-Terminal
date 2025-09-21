#!/bin/bash

# Simple Terminal Launcher
echo "🚀 Starting Simple Python Terminal..."

# Check if psutil is installed
python3 -c "import psutil" 2>/dev/null || {
    echo "📦 Installing required dependency: psutil"
    pip3 install psutil
}

# Run the terminal
python3 simple_terminal.py
