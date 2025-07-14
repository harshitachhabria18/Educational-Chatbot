# Educational-Chatbot
An AI-powered chatbot web application built using Flask, Google Gemini API, and HTML/CSS that answers educational questions only. The chatbot features voice input, session-based chat history, and automatic question classification to ensure responses remain focused on academic topics like science, math, history, and language learning.

# Features
Voice Input: Users can speak questions using the browser mic via Web Speech API.

Educational Question Filter: Questions are first classified using Gemini to check if they are academic in nature.

AI-Powered Answers: Uses Gemini 2.5 Flash to generate relevant and accurate educational responses.

Concise Mode: Optional checkbox to get short and to-the-point answers.

Session-Based History: Maintains Q&A history during the session for a better chat experience.

User-Friendly UI: Responsive layout with clean UI built using HTML, CSS, and vanilla JavaScript.

# Tech Stack
Backend: Flask (Python)

Frontend: HTML, CSS, Bootstrap (optional), JavaScript

AI Model: Google Gemini API

Voice Recognition: Web Speech API

Session Management: Flask session for storing chat history

# How to Run
1. Clone the repo 
  https://github.com/harshitachhabria18/Educational-Chatbot

2. Install dependencies
  (Ensure you have Python 3 and pip installed)

3. Set your Gemini API key in the code:
   genai.configure(api_key="YOUR_GEMINI_API_KEY")

4. Run the Flask app
   python app.py

5. Open in browser:
   http://localhost:5000


