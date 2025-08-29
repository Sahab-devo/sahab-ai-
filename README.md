# sahab-ai-
ai powered by google gemini
Sahab AI
AI chatbot with Gemini backend, available as a web app or desktop application. This guide helps you set up and run Sahab AI with zero prior experience required.

Features
Web app with chat interface.

Google Gemini AI backend integration.

Optionally runs as a native desktop app.

Prerequisites
Python 3.7 or newer must be installed.
How to check:
Run python --version in your terminal or command prompt.

Internet connection (for installing dependencies and AI service).

All project files (app.py, run_sahab_ai.py, requirements.txt) in the same folder.

Step 1: Download and Prepare All Files
Place the Sahab AI files in one directory:

app.py

run_sahab_ai.py

requirements.txt

(Optional: desktop_app.py for desktop mode)

Step 2: Install Python (if needed)
If Python is not installed, download and install it from python.org.

Step 3: Install Required Libraries
Open your command prompt or terminal.

Change into your project directory.

text
cd path/to/your/project
Run the setup script:

text
python run_sahab_ai.py
This will install all required packages automatically using requirements.txt.

Step 4: Configure Gemini API Key
The Gemini API key is already set in app.py (GEMINI_API_KEY).

No additional steps are needed unless you wish to use your own key; edit the line in app.py if required.

Step 5: Launch Sahab AI
When prompted:

text
🚀 Choose Sahab AI Version:
1. Web Version (Flask Server)
2. Desktop Application
Enter 1 to start the web app (best for beginners).

Enter 2 for desktop app (requires desktop_app.py and PyQt).

The web app launches automatically at http://localhost:5000. If your browser doesn’t open, copy-paste that address into it.

Step 6: Start Chatting!
Use the chat interface in your browser.

Just enter questions or prompts and receive instant AI-powered answers using Google Gemini.

Troubleshooting
Python version errors: Upgrade Python to 3.7 or newer.

Missing dependencies: Check your internet connection and ensure requirements.txt exists.

Missing index.html: Ensure there is a templates/index.html file as it is required for the web frontend.

App not opening in browser: Manually open http://localhost:5000.

FAQ
Question	Answer
Python version?	Python 3.7 or higher.
How to start?	Run python run_sahab_ai.py.
App address?	http://localhost:5000.
Desktop mode?	Enter 2 at launch (needs desktop_app.py).
Re-install libraries?	Rerun the setup script.
Support
If you see errors, carefully read the messages printed in your terminal.

Most issues can be solved by checking file placement, Python version, and internet connection.

Enjoy chatting with Sahab AI!





