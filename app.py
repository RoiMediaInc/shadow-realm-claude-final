from flask import Flask, request, jsonify
import os

app = Flask(__name__)
@app.route('/')
def home():
    return "✅ Backend is running on Render - Claude + ElevenLabs (Shadow Realm)"

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return "✅ Backend is running - Claude + ElevenLabs (Clean - New Service)"
    
    # Handle POST requests from the frontend
    try:
        character = request.form.get('character', 'Unknown')
        message = request.form.get('message', '')
        
        print(f"Received message from {character}: {message}")
        
        # TODO: Add your actual Claude logic here later
        reply = f"Hello! This is {character} speaking. You said: '{message}'. I'm currently in test mode."
        
        return jsonify({"reply": reply})
        
    except Exception as e:
        print("Error:", str(e))
        return jsonify({"reply": "Sorry, something went wrong on my end."}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
