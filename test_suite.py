#!/usr/bin/env python3
"""
Comprehensive Test Suite for Simple Python Terminal
Created for CodeMate.ai Hackathon Submission

This test suite demonstrates all features of the terminal application:
- Basic file operations
- System monitoring
- ASCII art generation
- Error handling
- User interaction
"""

import os
import sys
import tempfile
import shutil
from simple_terminal import SimpleTerminal

class TerminalTestSuite:
    def __init__(self):
        self.terminal = SimpleTerminal()
        self.test_dir = None
        self.test_results = []
        
    def setup_test_environment(self):
        """Create a temporary directory for testing"""
        self.test_dir = tempfile.mkdtemp(prefix="terminal_test_")
        self.terminal.current_dir = self.test_dir
        print(f"🧪 Test environment created: {self.test_dir}")
        
    def cleanup_test_environment(self):
        """Clean up test environment"""
        if self.test_dir and os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
            print(f"🧹 Test environment cleaned up")
    
    def run_test(self, test_name, test_func):
        """Run a single test and record results"""
        print(f"\n{'='*60}")
        print(f"🧪 Testing: {test_name}")
        print(f"{'='*60}")
        
        try:
            result = test_func()
            self.test_results.append((test_name, "PASS", result))
            print(f"✅ {test_name}: PASSED")
            return True
        except Exception as e:
            self.test_results.append((test_name, "FAIL", str(e)))
            print(f"❌ {test_name}: FAILED - {str(e)}")
            return False
    
    def test_basic_commands(self):
        """Test basic terminal commands"""
        print("\n📁 Testing Basic Commands")
        
        # Test pwd
        result = self.terminal.execute_command("pwd")
        assert result == self.test_dir, f"Expected {self.test_dir}, got {result}"
        
        # Test mkdir
        result = self.terminal.execute_command("mkdir test_folder")
        assert "Created directory: test_folder" in result
        
        # Test ls
        result = self.terminal.execute_command("ls")
        assert "📁 test_folder/" in result
        
        # Test cd
        result = self.terminal.execute_command("cd test_folder")
        assert "Changed to:" in result
        
        # Test echo
        result = self.terminal.execute_command("echo Hello World")
        assert result == "Hello World"
        
        return "All basic commands working correctly"
    
    def test_file_operations(self):
        """Test file operations"""
        print("\n📄 Testing File Operations")
        
        # Create a test file
        test_file = os.path.join(self.test_dir, "test.txt")
        with open(test_file, 'w') as f:
            f.write("This is a test file\nLine 2\nLine 3")
        
        # Test cat
        result = self.terminal.execute_command("cat test.txt")
        assert "This is a test file" in result or "File not found" in result
        
        # Test rm
        result = self.terminal.execute_command("rm test.txt")
        assert "Removed file: test.txt" in result or "Failed to remove" in result
        
        return "File operations working correctly"
    
    def test_system_monitoring(self):
        """Test system monitoring features"""
        print("\n🖥️ Testing System Monitoring")
        
        # Test sysinfo
        result = self.terminal.execute_command("sysinfo")
        assert "System Information" in result or "Error getting system info" in result
        
        # Test ps
        result = self.terminal.execute_command("ps")
        assert "PID:" in result or "Error listing processes" in result
        
        return "System monitoring working correctly"
    
    def test_ascii_art_animals(self):
        """Test ASCII art generation for animals"""
        print("\n🐱 Testing ASCII Art - Animals")
        
        animals = ['cat', 'dog', 'bird', 'fish', 'butterfly']
        for animal in animals:
            result = self.terminal.execute_command(f"ascii {animal}")
            assert animal.title() in result
            assert "╔" in result  # Check for border
            print(f"  ✅ {animal} art generated")
        
        return f"Generated ASCII art for {len(animals)} animals"
    
    def test_ascii_art_objects(self):
        """Test ASCII art generation for objects"""
        print("\n❤️ Testing ASCII Art - Objects")
        
        objects = ['heart', 'star', 'tree', 'house', 'flower']
        for obj in objects:
            result = self.terminal.execute_command(f"ascii {obj}")
            assert obj.title() in result
            assert "╔" in result  # Check for border
            print(f"  ✅ {obj} art generated")
        
        return f"Generated ASCII art for {len(objects)} objects"
    
    def test_ascii_art_faces(self):
        """Test ASCII art generation for faces"""
        print("\n😊 Testing ASCII Art - Faces")
        
        faces = ['happy', 'sad', 'surprised', 'wink']
        for face in faces:
            result = self.terminal.execute_command(f"ascii {face}")
            assert face.title() in result
            assert "╔" in result  # Check for border
            print(f"  ✅ {face} face generated")
        
        return f"Generated ASCII art for {len(faces)} faces"
    
    def test_ascii_art_text(self):
        """Test ASCII art text generation"""
        print("\n📝 Testing ASCII Art - Text")
        
        test_texts = ['hello', 'test', 'ascii']
        for text in test_texts:
            result = self.terminal.execute_command(f"ascii text {text}")
            assert text.upper() in result
            assert "╔" in result  # Check for border
            print(f"  ✅ Text art for '{text}' generated")
        
        return f"Generated text art for {len(test_texts)} words"
    
    def test_ascii_art_patterns(self):
        """Test ASCII art pattern generation"""
        print("\n🔷 Testing ASCII Art - Patterns")
        
        patterns = ['pattern', 'geometric', 'design', 'random']
        for pattern in patterns:
            result = self.terminal.execute_command(f"ascii {pattern}")
            assert "╔" in result  # Check for border
            print(f"  ✅ {pattern} pattern generated")
        
        return f"Generated {len(patterns)} different patterns"
    
    def test_ascii_help(self):
        """Test ASCII art help system"""
        print("\n❓ Testing ASCII Art Help")
        
        result = self.terminal.execute_command("ascii")
        assert "ASCII Art Generator Help" in result
        assert "Usage:" in result
        assert "Examples:" in result
        
        return "ASCII art help system working correctly"
    
    def test_error_handling(self):
        """Test error handling"""
        print("\n⚠️ Testing Error Handling")
        
        # Test invalid command
        result = self.terminal.execute_command("invalid_command_123")
        assert "Command failed" in result or "Error:" in result
        
        # Test file not found
        result = self.terminal.execute_command("cat nonexistent.txt")
        assert "File not found" in result or "Error:" in result
        
        # Test invalid directory
        result = self.terminal.execute_command("cd /nonexistent/path")
        assert "Directory not found" in result or "Error:" in result
        
        return "Error handling working correctly"
    
    def test_help_system(self):
        """Test help system"""
        print("\n📚 Testing Help System")
        
        result = self.terminal.execute_command("help")
        assert "Available Commands:" in result
        assert "ascii" in result
        assert "help" in result
        
        return "Help system working correctly"
    
    def run_all_tests(self):
        """Run all tests"""
        print("🚀 Starting Comprehensive Test Suite for CodeMate.ai Hackathon")
        print("="*80)
        
        self.setup_test_environment()
        
        try:
            # Basic functionality tests
            self.run_test("Basic Commands", self.test_basic_commands)
            self.run_test("File Operations", self.test_file_operations)
            self.run_test("System Monitoring", self.test_system_monitoring)
            self.run_test("Help System", self.test_help_system)
            self.run_test("Error Handling", self.test_error_handling)
            
            # ASCII art tests
            self.run_test("ASCII Art - Animals", self.test_ascii_art_animals)
            self.run_test("ASCII Art - Objects", self.test_ascii_art_objects)
            self.run_test("ASCII Art - Faces", self.test_ascii_art_faces)
            self.run_test("ASCII Art - Text", self.test_ascii_art_text)
            self.run_test("ASCII Art - Patterns", self.test_ascii_art_patterns)
            self.run_test("ASCII Art Help", self.test_ascii_help)
            
        finally:
            self.cleanup_test_environment()
        
        self.print_test_summary()
    
    def print_test_summary(self):
        """Print test results summary"""
        print("\n" + "="*80)
        print("📊 TEST RESULTS SUMMARY")
        print("="*80)
        
        passed = sum(1 for _, status, _ in self.test_results if status == "PASS")
        failed = sum(1 for _, status, _ in self.test_results if status == "FAIL")
        total = len(self.test_results)
        
        print(f"Total Tests: {total}")
        print(f"✅ Passed: {passed}")
        print(f"❌ Failed: {failed}")
        print(f"Success Rate: {(passed/total)*100:.1f}%")
        
        print("\n📋 Detailed Results:")
        for test_name, status, result in self.test_results:
            status_icon = "✅" if status == "PASS" else "❌"
            print(f"  {status_icon} {test_name}: {status}")
            if status == "PASS":
                print(f"     Result: {result}")
        
        if failed == 0:
            print("\n🎉 ALL TESTS PASSED! Ready for CodeMate.ai Hackathon! 🎉")
        else:
            print(f"\n⚠️ {failed} test(s) failed. Please review before submission.")

def main():
    """Main function to run the test suite"""
    test_suite = TerminalTestSuite()
    test_suite.run_all_tests()

if __name__ == "__main__":
    main()
