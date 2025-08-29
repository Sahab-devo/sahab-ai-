# app.py - Flask Backend Server
import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import threading
import time

# Configure Gemini API Key
GEMINI_API_KEY = "AIzaSyCskoz7K21zG7DAmGs0puXNyYJ-XqYwjOo"
genai.configure(api_key=GEMINI_API_KEY)

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

def get_gemini_response(prompt):
    """Get response from Gemini AI"""
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text or "I apologize, but I couldn't generate a response. Please try again."
    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        return f"Error: Unable to connect to AI service. Please check your API key and try again."

@app.route('/')
def index():
    """Serve the main HTML page"""
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat API requests"""
    try:
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({'error': 'No message provided'}), 400
        
        user_message = data['message'].strip()
        if not user_message:
            return jsonify({'error': 'Empty message'}), 400
        
        # Get AI response
        ai_response = get_gemini_response(user_message)
        
        return jsonify({
            'response': ai_response,
            'status': 'success'
        })
        
    except Exception as e:
        print(f"Error in chat endpoint: {e}")
        return jsonify({
            'error': 'Internal server error',
            'status': 'error'
        }), 500

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'service': 'Sahab AI Backend'})

if __name__ == '__main__':
    print("🚀 Starting Sahab AI Full Stack Application...")
    print("💫 3D Frontend: Stunning visual interface")
    print("🤖 AI Backend: Google Gemini Integration")
    print("🌐 Access your app at: http://localhost:5000")
    print("-" * 50)
    
    # Create templates directory if it doesn't exist
    os.makedirs('templates', exist_ok=True)
    
    # Run the Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)