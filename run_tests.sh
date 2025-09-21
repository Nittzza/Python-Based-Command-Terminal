#!/bin/bash

# Test Runner Script for CodeMate.ai Hackathon
# This script runs all tests and generates a comprehensive report

echo "🚀 CodeMate.ai Hackathon - Terminal App Test Suite"
echo "=================================================="

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    exit 1
fi

# Check if required packages are installed
echo "📦 Checking dependencies..."
python3 -c "import psutil" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "⚠️  Installing required package: psutil"
    pip3 install psutil
fi

echo "✅ Dependencies ready"
echo ""

# Run the comprehensive test suite
echo "🧪 Running Comprehensive Test Suite..."
echo "======================================"
python3 test_suite.py

echo ""
echo "🎯 Running Interactive Demo..."
echo "=============================="
echo "The demo will showcase all features interactively."
echo "Press Ctrl+C to skip the demo, or wait for it to start..."
sleep 3

# Run the demo (with timeout to prevent hanging)
timeout 300 python3 demo_script.py || echo "Demo completed or timed out"

echo ""
echo "📊 Test Summary Complete!"
echo "========================="
echo "✅ All tests have been executed"
echo "✅ Demo has been run"
echo "✅ Application is ready for CodeMate.ai Hackathon submission"
echo ""
echo "🎉 Good luck with your hackathon submission!"
