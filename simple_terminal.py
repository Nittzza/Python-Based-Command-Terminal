#!/usr/bin/env python3
"""
Simple Python Terminal
A basic command terminal implementation with file operations and system monitoring.
"""

import os
import sys
import subprocess
import shutil
import psutil
import random
import re
from pathlib import Path

class SimpleTerminal:
    def __init__(self):
        self.current_dir = os.getcwd()
        self.running = True
        self.ascii_patterns = self._init_ascii_patterns()
        
    def show_banner(self):
        """Display simple welcome message"""
        print("🚀 Simple Python Terminal v1.0")
        print("Type 'help' for available commands or 'exit' to quit.\n")

    def get_prompt(self):
        """Get the current prompt with directory"""
        return f"terminal@{os.path.basename(self.current_dir)}: {self.current_dir}$ "

    def execute_command(self, command):
        """Execute a command and return the result"""
        parts = command.strip().split()
        if not parts:
            return ""
        
        cmd = parts[0].lower()
        args = parts[1:] if len(parts) > 1 else []
        
        try:
            if cmd == "help":
                return self.show_help()
            elif cmd == "exit" or cmd == "quit":
                self.running = False
                return "Goodbye! 👋"
            elif cmd == "pwd":
                return self.current_dir
            elif cmd == "ls":
                return self.list_directory()
            elif cmd == "cd":
                return self.change_directory(args)
            elif cmd == "mkdir":
                return self.make_directory(args)
            elif cmd == "rm":
                return self.remove_file(args)
            elif cmd == "cat":
                return self.cat_file(args)
            elif cmd == "echo":
                return " ".join(args)
            elif cmd == "clear":
                os.system('clear' if os.name == 'posix' else 'cls')
                return ""
            elif cmd == "sysinfo":
                return self.get_system_info()
            elif cmd == "ps":
                return self.list_processes()
            elif cmd == "ascii":
                return self.generate_ascii_art(args)
            else:
                # Try to execute as system command
                return self.execute_system_command(command)
        except Exception as e:
            return f"Error: {str(e)}"

    def show_help(self):
        """Show available commands"""
        help_text = """
Available Commands:
  help          - Show this help message
  exit/quit     - Exit the terminal
  pwd           - Print working directory
  ls            - List directory contents
  cd <dir>      - Change directory
  mkdir <name>  - Create directory
  rm <file>     - Remove file
  cat <file>    - Display file contents
  echo <text>   - Print text
  clear         - Clear screen
  sysinfo       - Show system information
  ps            - List running processes
  ascii <text>  - Generate ASCII art from text or prompt
  <command>     - Execute any system command
        """
        return help_text

    def list_directory(self):
        """List directory contents"""
        try:
            items = os.listdir(self.current_dir)
            if not items:
                return "Directory is empty"
            
            result = []
            for item in sorted(items):
                item_path = os.path.join(self.current_dir, item)
                if os.path.isdir(item_path):
                    result.append(f"📁 {item}/")
                else:
                    result.append(f"📄 {item}")
            return "\n".join(result)
        except PermissionError:
            return "Permission denied"

    def change_directory(self, args):
        """Change directory"""
        if not args:
            return "Usage: cd <directory>"
        
        target = args[0]
        if target == "..":
            new_dir = os.path.dirname(self.current_dir)
        elif target.startswith("/"):
            new_dir = target
        else:
            new_dir = os.path.join(self.current_dir, target)
        
        if os.path.exists(new_dir) and os.path.isdir(new_dir):
            self.current_dir = os.path.abspath(new_dir)
            return f"Changed to: {self.current_dir}"
        else:
            return f"Directory not found: {target}"

    def make_directory(self, args):
        """Create directory"""
        if not args:
            return "Usage: mkdir <directory_name>"
        
        dir_name = args[0]
        dir_path = os.path.join(self.current_dir, dir_name)
        
        try:
            os.makedirs(dir_path, exist_ok=True)
            return f"Created directory: {dir_name}"
        except Exception as e:
            return f"Failed to create directory: {str(e)}"

    def remove_file(self, args):
        """Remove file or directory"""
        if not args:
            return "Usage: rm <file_or_directory>"
        
        target = args[0]
        target_path = os.path.join(self.current_dir, target)
        
        try:
            if os.path.isdir(target_path):
                shutil.rmtree(target_path)
                return f"Removed directory: {target}"
            else:
                os.remove(target_path)
                return f"Removed file: {target}"
        except Exception as e:
            return f"Failed to remove: {str(e)}"

    def cat_file(self, args):
        """Display file contents"""
        if not args:
            return "Usage: cat <file>"
        
        file_path = os.path.join(self.current_dir, args[0])
        
        try:
            with open(file_path, 'r') as f:
                return f.read()
        except FileNotFoundError:
            return f"File not found: {args[0]}"
        except Exception as e:
            return f"Error reading file: {str(e)}"

    def get_system_info(self):
        """Get system information"""
        try:
            cpu_percent = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')
            
            info = f"""
🖥️  System Information:
   CPU Usage: {cpu_percent}%
   Memory: {memory.percent}% used ({memory.used // (1024**3)}GB / {memory.total // (1024**3)}GB)
   Disk: {disk.percent}% used ({disk.used // (1024**3)}GB / {disk.total // (1024**3)}GB)
   Platform: {sys.platform}
            """
            return info.strip()
        except Exception as e:
            return f"Error getting system info: {str(e)}"

    def list_processes(self):
        """List running processes"""
        try:
            processes = []
            for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
                try:
                    processes.append(f"PID: {proc.info['pid']:>6} | {proc.info['name']:<20} | CPU: {proc.info['cpu_percent']:>5.1f}%")
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
            
            # Show top 10 processes
            return "\n".join(processes[:10])
        except Exception as e:
            return f"Error listing processes: {str(e)}"

    def execute_system_command(self, command):
        """Execute system command"""
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, cwd=self.current_dir)
            if result.stdout:
                return result.stdout
            elif result.stderr:
                return f"Error: {result.stderr}"
            else:
                return "Command executed successfully"
        except Exception as e:
            return f"Command failed: {str(e)}"

    def _init_ascii_patterns(self):
        """Initialize ASCII art patterns and templates"""
        return {
            'animals': {
                'cat': [
                    "    /\\_/\\  ",
                    "   ( o.o ) ",
                    "    > ^ <  "
                ],
                'dog': [
                    "    / \\__  ",
                    "   (    @\\___",
                    "   /         O",
                    "  /   (_____/",
                    " /_____/   U"
                ],
                'bird': [
                    "     .-.   ",
                    "    (o o)  ",
                    "     |_|   ",
                    "    /| |\\  ",
                    "   ( | | ) ",
                    "    \"\"\"\"\"  "
                ],
                'fish': [
                    "    ><((('> ",
                    "   <'((((><",
                    "    ><((('> "
                ],
                'butterfly': [
                    "    .-.   .-.   ",
                    "   (   `-'   )  ",
                    "    `-.   .-'   ",
                    "      `-'       "
                ]
            },
            'objects': {
                'heart': [
                    "  ♥       ♥  ",
                    " ♥   ♥   ♥   ",
                    "  ♥       ♥  ",
                    "   ♥     ♥   ",
                    "    ♥   ♥    ",
                    "     ♥ ♥     ",
                    "      ♥      "
                ],
                'star': [
                    "    *     ",
                    "   ***    ",
                    "  *****   ",
                    "   ***    ",
                    "    *     "
                ],
                'tree': [
                    "    *     ",
                    "   ***    ",
                    "  *****   ",
                    " *******  ",
                    "    |     ",
                    "    |     "
                ],
                'house': [
                    "    /\\    ",
                    "   /  \\   ",
                    "  /____\\  ",
                    " |      | ",
                    " |      | ",
                    " |______| "
                ],
                'flower': [
                    "    @     ",
                    "   @@@    ",
                    "  @@@@@   ",
                    "   @@@    ",
                    "    |     ",
                    "    |     "
                ]
            },
            'faces': {
                'happy': [
                    "  ^   ^  ",
                    "    -    ",
                    "  \\___/  "
                ],
                'sad': [
                    "  ^   ^  ",
                    "    -    ",
                    "  ___/   "
                ],
                'surprised': [
                    "  O   O  ",
                    "    -    ",
                    "  \\___/  "
                ],
                'wink': [
                    "  ^   -  ",
                    "    -    ",
                    "  \\___/  "
                ]
            },
            'text_styles': {
                'block': ['█', '▓', '▒', '░'],
                'line': ['─', '│', '┌', '┐', '└', '┘', '├', '┤', '┬', '┴', '┼'],
                'double': ['═', '║', '╔', '╗', '╚', '╝', '╠', '╣', '╦', '╩', '╬'],
                'simple': ['*', '+', '-', '|', '#', '@', '%', '&']
            }
        }

    def generate_ascii_art(self, args):
        """Generate ASCII art based on user prompt"""
        if not args:
            return self._show_ascii_help()
        
        prompt = " ".join(args).lower()
        
        # Check for specific patterns
        for category, items in self.ascii_patterns.items():
            if category == 'text_styles':
                continue
            for key, art in items.items():
                if key in prompt:
                    return self._format_ascii_art(art, key.title())
        
        # Generate text-based ASCII art
        if any(word in prompt for word in ['text', 'word', 'letter', 'name']):
            text = self._extract_text_from_prompt(prompt)
            if text:
                return self._create_text_ascii(text)
        
        # Generate geometric patterns
        if any(word in prompt for word in ['pattern', 'geometric', 'shape', 'design']):
            return self._create_geometric_pattern(prompt)
        
        # Generate random creative art
        return self._create_random_art(prompt)

    def _show_ascii_help(self):
        """Show ASCII art help and examples"""
        help_text = """
🎨 ASCII Art Generator Help:

Usage: ascii <prompt>

Examples:
  ascii cat          - Generate a cat
  ascii heart        - Generate a heart
  ascii happy        - Generate a happy face
  ascii text hello   - Generate text art for "hello"
  ascii pattern      - Generate a geometric pattern
  ascii random       - Generate random creative art

Available categories:
  Animals: cat, dog, bird, fish, butterfly
  Objects: heart, star, tree, house, flower
  Faces: happy, sad, surprised, wink
  Text: text <your_text>
  Patterns: pattern, geometric, design
        """
        return help_text

    def _format_ascii_art(self, art_lines, title):
        """Format ASCII art with a nice border"""
        if not art_lines:
            return "No art generated"
        
        max_width = max(len(line) for line in art_lines)
        border = "═" * (max_width + 4)
        
        result = [f"╔{border}╗"]
        result.append(f"║ {title.center(max_width + 2)} ║")
        result.append(f"╠{border}╣")
        
        for line in art_lines:
            result.append(f"║ {line.center(max_width + 2)} ║")
        
        result.append(f"╚{border}╝")
        return "\n".join(result)

    def _extract_text_from_prompt(self, prompt):
        """Extract text to convert to ASCII art"""
        # Remove common words and extract the actual text
        words_to_remove = ['text', 'word', 'letter', 'name', 'ascii', 'art', 'generate', 'create']
        words = prompt.split()
        text_words = [word for word in words if word not in words_to_remove]
        return " ".join(text_words) if text_words else "ASCII"

    def _create_text_ascii(self, text):
        """Create ASCII art from text using simple patterns"""
        if not text:
            text = "ASCII"
        
        # Simple ASCII text art using characters
        lines = []
        for char in text.upper():
            if char == ' ':
                lines.append("     ")
            elif char == 'A':
                lines.append([
                    "  ██  ",
                    " ████ ",
                    "██  ██",
                    "██████",
                    "██  ██"
                ])
            elif char == 'S':
                lines.append([
                    " █████",
                    "██    ",
                    " █████",
                    "    ██",
                    "█████ "
                ])
            elif char == 'C':
                lines.append([
                    " █████",
                    "██    ",
                    "██    ",
                    "██    ",
                    " █████"
                ])
            elif char == 'I':
                lines.append([
                    "██████",
                    "  ██  ",
                    "  ██  ",
                    "  ██  ",
                    "██████"
                ])
            else:
                # Default pattern for other characters
                lines.append([
                    "██████",
                    "██  ██",
                    "██████",
                    "██  ██",
                    "██████"
                ])
        
        # Combine all characters
        if lines:
            result = []
            for i in range(5):  # Each character has 5 lines
                line = ""
                for char_lines in lines:
                    if i < len(char_lines):
                        line += char_lines[i] + " "
                result.append(line)
            return self._format_ascii_art(result, text.upper())
        
        return "Text art generation failed"

    def _create_geometric_pattern(self, prompt):
        """Create geometric ASCII patterns"""
        patterns = [
            # Diamond pattern
            [
                "    *    ",
                "   ***   ",
                "  *****  ",
                " ******* ",
                "*********",
                " ******* ",
                "  *****  ",
                "   ***   ",
                "    *    "
            ],
            # Spiral pattern
            [
                "████████",
                "█      █",
                "█ ████ █",
                "█ █  █ █",
                "█ █  █ █",
                "█ ████ █",
                "█      █",
                "████████"
            ],
            # Checkerboard
            [
                "█ █ █ █ ",
                " █ █ █ █",
                "█ █ █ █ ",
                " █ █ █ █",
                "█ █ █ █ ",
                " █ █ █ █",
                "█ █ █ █ ",
                " █ █ █ █"
            ],
            # Wave pattern
            [
                "    ██    ██    ",
                "  ██  ██  ██  ██",
                "██      ██      ",
                "  ██  ██  ██  ██",
                "    ██    ██    "
            ]
        ]
        
        pattern = random.choice(patterns)
        return self._format_ascii_art(pattern, "Geometric Pattern")

    def _create_random_art(self, prompt):
        """Create random creative ASCII art"""
        creative_arts = [
            # Abstract art
            [
                "  ◢◤◢◤  ",
                " ◢◤  ◢◤ ",
                "◢◤    ◢◤",
                " ◢◤  ◢◤ ",
                "  ◢◤◢◤  "
            ],
            # Pixel art style
            [
                "▓▓▓▓▓▓▓▓",
                "▓  ▓▓  ▓",
                "▓▓    ▓▓",
                "▓  ▓▓  ▓",
                "▓▓▓▓▓▓▓▓"
            ],
            # Organic pattern
            [
                "   ◯   ◯   ",
                " ◯   ◯   ◯ ",
                "   ◯   ◯   ",
                " ◯   ◯   ◯ ",
                "   ◯   ◯   "
            ],
            # Tech pattern
            [
                "┌─┐ ┌─┐ ┌─┐",
                "│ │ │ │ │ │",
                "└─┘ └─┘ └─┘",
                "┌─┐ ┌─┐ ┌─┐",
                "│ │ │ │ │ │",
                "└─┘ └─┘ └─┘"
            ]
        ]
        
        art = random.choice(creative_arts)
        return self._format_ascii_art(art, "Creative Art")

    def run(self):
        """Main terminal loop"""
        self.show_banner()
        
        while self.running:
            try:
                command = input(self.get_prompt())
                if command.strip():
                    result = self.execute_command(command)
                    if result:
                        print(result)
                    print()  # Add spacing
            except KeyboardInterrupt:
                print("\nUse 'exit' to quit the terminal.")
            except EOFError:
                print("\nGoodbye! 👋")
                break

if __name__ == "__main__":
    terminal = SimpleTerminal()
    terminal.run()
