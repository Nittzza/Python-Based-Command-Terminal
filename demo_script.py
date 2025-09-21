#!/usr/bin/env python3
"""
Interactive Demo Script for Simple Python Terminal
Created for CodeMate.ai Hackathon Presentation

This script provides an automated demonstration of all terminal features
with explanations and examples perfect for judges and audience.
"""

import time
import os
import sys
from simple_terminal import SimpleTerminal

class TerminalDemo:
    def __init__(self):
        self.terminal = SimpleTerminal()
        
    def print_section(self, title, description=""):
        """Print a formatted section header"""
        print("\n" + "="*80)
        print(f"🎯 {title}")
        if description:
            print(f"   {description}")
        print("="*80)
        time.sleep(1)
    
    def demo_basic_commands(self):
        """Demonstrate basic terminal commands"""
        self.print_section("BASIC TERMINAL COMMANDS", "Core file system operations")
        
        commands = [
            ("pwd", "Show current directory"),
            ("ls", "List directory contents"),
            ("mkdir demo_folder", "Create a new directory"),
            ("cd demo_folder", "Change to the new directory"),
            ("echo 'Hello CodeMate!'", "Display text"),
            ("cd ..", "Go back to parent directory")
        ]
        
        for cmd, description in commands:
            print(f"\n💡 {description}")
            print(f"Command: {cmd}")
            print("-" * 40)
            result = self.terminal.execute_command(cmd)
            if result:
                print(result)
            time.sleep(1.5)
    
    def demo_file_operations(self):
        """Demonstrate file operations"""
        self.print_section("FILE OPERATIONS", "Creating, reading, and managing files")
        
        # Create a demo file
        demo_file = os.path.join(self.terminal.current_dir, "demo.txt")
        with open(demo_file, 'w') as f:
            f.write("Welcome to CodeMate.ai Hackathon!\n")
            f.write("This is a demo file created by our terminal.\n")
            f.write("Line 3: ASCII art generation is amazing!\n")
        
        commands = [
            ("ls", "List files (including our demo file)"),
            ("cat demo.txt", "Display file contents"),
            ("echo 'New line' >> demo.txt", "Append to file"),
            ("cat demo.txt", "Show updated file contents"),
            ("rm demo.txt", "Remove the demo file")
        ]
        
        for cmd, description in commands:
            print(f"\n💡 {description}")
            print(f"Command: {cmd}")
            print("-" * 40)
            result = self.terminal.execute_command(cmd)
            if result:
                print(result)
            time.sleep(1.5)
    
    def demo_system_monitoring(self):
        """Demonstrate system monitoring features"""
        self.print_section("SYSTEM MONITORING", "Real-time system information")
        
        commands = [
            ("sysinfo", "Display system information (CPU, Memory, Disk)"),
            ("ps", "Show running processes")
        ]
        
        for cmd, description in commands:
            print(f"\n💡 {description}")
            print(f"Command: {cmd}")
            print("-" * 40)
            result = self.terminal.execute_command(cmd)
            if result:
                print(result)
            time.sleep(2)
    
    def demo_ascii_art_animals(self):
        """Demonstrate ASCII art generation for animals"""
        self.print_section("ASCII ART - ANIMALS", "Creative ASCII art generation")
        
        animals = [
            ("cat", "A cute ASCII cat"),
            ("dog", "A friendly ASCII dog"),
            ("butterfly", "A beautiful ASCII butterfly")
        ]
        
        for animal, description in animals:
            print(f"\n💡 {description}")
            print(f"Command: ascii {animal}")
            print("-" * 40)
            result = self.terminal.execute_command(f"ascii {animal}")
            if result:
                print(result)
            time.sleep(2)
    
    def demo_ascii_art_objects(self):
        """Demonstrate ASCII art generation for objects"""
        self.print_section("ASCII ART - OBJECTS", "Various object designs")
        
        objects = [
            ("heart", "A beautiful heart shape"),
            ("star", "A classic star design"),
            ("tree", "A simple tree")
        ]
        
        for obj, description in objects:
            print(f"\n💡 {description}")
            print(f"Command: ascii {obj}")
            print("-" * 40)
            result = self.terminal.execute_command(f"ascii {obj}")
            if result:
                print(result)
            time.sleep(2)
    
    def demo_ascii_art_text(self):
        """Demonstrate ASCII text art generation"""
        self.print_section("ASCII TEXT ART", "Convert text to stylized ASCII art")
        
        texts = [
            ("text CODEMATE", "Convert 'CODEMATE' to ASCII art"),
            ("text HACKATHON", "Convert 'HACKATHON' to ASCII art")
        ]
        
        for text_cmd, description in texts:
            print(f"\n💡 {description}")
            print(f"Command: ascii {text_cmd}")
            print("-" * 40)
            result = self.terminal.execute_command(f"ascii {text_cmd}")
            if result:
                print(result)
            time.sleep(2)
    
    def demo_ascii_art_patterns(self):
        """Demonstrate pattern generation"""
        self.print_section("ASCII PATTERNS", "Geometric and creative patterns")
        
        patterns = [
            ("pattern", "Generate a geometric pattern"),
            ("random", "Generate random creative art")
        ]
        
        for pattern, description in patterns:
            print(f"\n💡 {description}")
            print(f"Command: ascii {pattern}")
            print("-" * 40)
            result = self.terminal.execute_command(f"ascii {pattern}")
            if result:
                print(result)
            time.sleep(2)
    
    def demo_help_system(self):
        """Demonstrate help system"""
        self.print_section("HELP SYSTEM", "Built-in documentation and guidance")
        
        print("\n💡 View all available commands")
        print("Command: help")
        print("-" * 40)
        result = self.terminal.execute_command("help")
        if result:
            print(result)
        time.sleep(2)
        
        print("\n💡 ASCII art help and examples")
        print("Command: ascii")
        print("-" * 40)
        result = self.terminal.execute_command("ascii")
        if result:
            print(result)
        time.sleep(2)
    
    def run_full_demo(self):
        """Run the complete demonstration"""
        print("🚀 WELCOME TO SIMPLE PYTHON TERMINAL DEMO")
        print("🎯 Created for CodeMate.ai Hackathon")
        print("="*80)
        print("This demo showcases all features of our terminal application:")
        print("• Basic file operations")
        print("• System monitoring")
        print("• Creative ASCII art generation")
        print("• Help system and error handling")
        print("="*80)
        
        input("\nPress Enter to start the demonstration...")
        
        # Run all demo sections
        self.demo_basic_commands()
        self.demo_file_operations()
        self.demo_system_monitoring()
        self.demo_ascii_art_animals()
        self.demo_ascii_art_objects()
        self.demo_ascii_art_text()
        self.demo_ascii_art_patterns()
        self.demo_help_system()
        
        # Final summary
        self.print_section("DEMO COMPLETE", "Thank you for watching!")
        print("🎉 This terminal application demonstrates:")
        print("   ✅ Complete file system operations")
        print("   ✅ Real-time system monitoring")
        print("   ✅ Creative ASCII art generation")
        print("   ✅ User-friendly help system")
        print("   ✅ Robust error handling")
        print("\n🏆 Ready for CodeMate.ai Hackathon submission!")
        print("="*80)

def main():
    """Main function to run the demo"""
    demo = TerminalDemo()
    demo.run_full_demo()

if __name__ == "__main__":
    main()
