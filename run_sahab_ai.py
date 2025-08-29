
  

#!/usr/bin/env python3
"""
Sahab AI - Full Stack Setup Script
This script sets up and runs either the web or desktop version of Sahab AI
"""

import os
import sys
import subprocess
import webbrowser
import time
from pathlib import Path

# ...existing code...


def launch_desktop():
    """Launch the desktop version"""
    print("\n🖥️  Launching Desktop Version...")
    try:
        from desktop_app import main
        main()
    except ImportError:
        print("❌ desktop_app.py not found or dependencies missing.")
        return False
    return True

def main():
    """Main setup function"""
    print_banner()
    
    # Check system requirements
    if not check_python():
        return
    
    # Create directories
    create_directories()
    
    # Install requirements
    if not install_requirements():
        return
    
    # Check API key
    check_api_key()
    
    # Ask user which version to launch
    print("\n🚀 Choose Sahab AI Version:")
    print("1. Web Version (Flask Server)")
    print("2. Desktop Application")
    
    choice = input("\nEnter your choice (1 or 2): ").strip()
    
    if choice == "1":
        # Start the web server
        print("\n🌐 Starting Web Version...")
        start_server()
    elif choice == "2":
        # Launch desktop version
        launch_desktop()
    else:
        print("❌ Invalid choice. Please enter 1 or 2.")

# ...rest of existing code...#!/usr/bin/env python3
"""
Sahab AI - Full Stack Setup Script
This script sets up and runs the complete Sahab AI application
"""

import os
import sys
import subprocess
import webbrowser
import time
from pathlib import Path

def print_banner():
    """Print a beautiful banner"""
    banner = """
╔═══════════════════════════════════════════════╗
║                                               ║
║    ✨ SAHAB AI - FULL STACK SETUP ✨          ║
║                                               ║
║    🚀 3D Frontend + Google Gemini Backend     ║
║    🌐 Flask Server + Beautiful UI             ║
║                                               ║
╚═══════════════════════════════════════════════╝
"""
    print(banner)

def check_python():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 7):
        print("❌ Python 3.7+ is required. Please upgrade Python.")
        return False
    print(f"✅ Python {sys.version.split()[0]} detected")
    return True

def install_requirements():
    """Install required packages"""
    print("\n📦 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ All packages installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install packages. Please check your internet connection.")
        return False
    except FileNotFoundError:
        print("❌ requirements.txt not found. Please ensure all files are in the same directory.")
        return False

def create_directories():
    """Create necessary directories"""
    print("\n📁 Setting up directory structure...")
    templates_dir = Path("templates")
    templates_dir.mkdir(exist_ok=True)
    print("✅ Directory structure created!")

def check_api_key():
    """Check if API key is configured"""
    api_key = "AIzaSyCskoz7K21zG7DAmGs0puXNyYJ-XqYwjOo"
    if api_key and api_key.startswith("AIzaSy"):
        print("✅ Gemini API key configured")
        return True
    else:
        print("⚠️  Please configure your Gemini API key in app.py")
        return False

def create_html_template():
    """Create the HTML template file"""
    print("\n📄 Creating HTML template...")
    templates_dir = Path("templates")
    html_file = templates_dir / "index.html"
    
    # The HTML content would be written here
    # For brevity, assuming it exists or will be copied
    if html_file.exists():
        print("✅ HTML template found!")
        return True
    else:
        print("⚠️  Please ensure index.html is in the templates/ directory")
        return False

def start_server():
    """Start the Flask server"""
    print("\n🚀 Starting Sahab AI server...")
    print("=" * 50)
    print("🌐 Server will start at: http://localhost:5000")
    print("✨ 3D Interface will load automatically")
    print("🤖 AI Backend: Google Gemini Integration")
    print("=" * 50)
    
    # Wait a moment then open browser
    def open_browser():
        time.sleep(3)
        webbrowser.open("http://localhost:5000")
    
    import threading
    browser_thread = threading.Thread(target=open_browser)
    browser_thread.daemon = True
    browser_thread.start()
    
    # Import and run the Flask app
    try:
        from app import app
        app.run(debug=True, host='0.0.0.0', port=5000, use_reloader=False)
    except ImportError:
        print("❌ app.py not found. Please ensure all files are in the same directory.")
        return False
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        return False

def main():
    """Main setup function"""
    print_banner()
    
    # Check system requirements
    if not check_python():
        return
    
    # Create directories
    create_directories()
    
    # Install requirements
    if not install_requirements():
        return
    
    # Check API key
    check_api_key()
    
    # Check template
    create_html_template()
    
    # Start the server
    print("\n🎯 Setup complete! Starting server...")
    input("Press Enter to start Sahab AI server...")
    start_server()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye! Thanks for using Sahab AI!")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        print("Please check the setup and try again.")