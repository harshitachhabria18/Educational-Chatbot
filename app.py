import os
import google.generativeai as genai
from dotenv import load_dotenv
from flask import Flask, request, render_template, session

# Load .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "fallback_secret_key")

# Configure Gemini API Key from .env
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

@app.route("/", methods=["GET"])
def index():
    # Load chat history from session (or start new)
    history = session.get("history", [])
    return render_template("form.html", history=history)

@app.route("/generate", methods=["POST"])
def generate():
    user_input = request.form.get("prompt", "").strip()
    concise = request.form.get("concise") == "yes"

    try:
        # Step 1: Classify if it's educational
        checker_model = genai.GenerativeModel("gemini-2.5-flash")
        classification_prompt = (
            "Answer only 'yes' or 'no'.\n"
            "Is the following question educational — meaning related to school subjects, academic topics, or learning? "
            "Educational topics include science, math, history, geography, language learning, etc. "
            "Do NOT say anything else.\n\n"
            f"Question: {user_input}"
        )
        check_response = checker_model.generate_content(classification_prompt)
        verdict = check_response.text.strip().lower()
    except Exception as e:
        return render_template("form.html", response=f"Error during classification: {str(e)}", history=session.get("history", []))

    history = session.get("history", [])

    if verdict != "yes":
        # Store non-educational question and response
        bot_reply = "❗ This chatbot only answers educational questions. Please ask something related to learning, subjects, or academics."
        history.append({"question": user_input, "answer": bot_reply})
        session["history"] = history
        return render_template("form.html", response="", history=history)

    # Step 2: Prepare system instruction
    system_instruction = (
        "You are an expert educational assistant. Only provide helpful, accurate answers "
        "on educational topics like science, history, mathematics, geography, and language learning."
    )

    if concise:
        system_instruction += " Keep your answer brief and to the point, but ensure all key points are covered."

    full_prompt = f"{system_instruction}\n\nUser: {user_input}"

    try:
        # Step 3: Generate educational response
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(full_prompt)
        answer = response.text
    except Exception as e:
        return render_template("form.html", response=f"Error generating response: {str(e)}", history=history)

    # Step 4: Save Q&A to history
    history.append({"question": user_input, "answer": answer})
    session["history"] = history

    return render_template("form.html", response=answer, history=history)

if __name__ == "__main__":
    app.run(debug=True)
