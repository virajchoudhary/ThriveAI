from flask import Flask, render_template, request, jsonify
from transformers import pipeline
import os

app = Flask(__name__)

# AI Emotion Classifier (Lightweight)
emotion_classifier = pipeline(
    "text-classification",
    model="bhadresh-savani/distilbert-base-uncased-emotion",
    top_k=1
)

RESPONSE_TEMPLATES = {
    "sadness": [
        "I sense you're feeling down. Try these steps:\n"
        "1. Deep breathing exercise (4-7-8 pattern)\n"
        "2. Write in a journal for 10 minutes\n"
        "3. Reach out to a trusted friend"
    ],
    "joy": [
        "Great to hear positive feelings!\n"
        "1. Savor this moment consciously\n"
        "2. Share your happiness with others\n"
        "3. Engage in a favorite activity"
    ],
    "anger": [
        "Let's help release this tension:\n"
        "1. Physical exercise (even 5 minutes)\n"
        "2. Progressive muscle relaxation\n"
        "3. Reframe the situation objectively"
    ],
    "fear": [
        "Anxiety management strategies:\n"
        "1. 5-4-3-2-1 grounding technique\n"
        "2. Challenge catastrophic thoughts\n"
        "3. Safe space visualization"
    ]
}

CRISIS_KEYWORDS = ["suicide", "kill myself", "self-harm"]

def generate_response(text):
    # Crisis detection
    if any(keyword in text.lower() for keyword in CRISIS_KEYWORDS):
        return {
            "message": "Immediate Help: 1-800-273-TALK (US)\n1. Stay in safe space\n2. Contact trusted person\n3. Seek professional care",
            "priority": "critical"
        }
    
    # AI emotion classification
    try:
        result = emotion_classifier(text)[0][0]
        emotion = result['label']
        return {
            "message": "\n".join(RESPONSE_TEMPLATES.get(emotion, ["How can I best support you?"])),
            "priority": "normal"
        }
    except:
        return {
            "message": "I'm here to listen. Could you share more?",
            "priority": "normal"
        }

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_input = request.json['message']
        return jsonify(generate_response(user_input))
    except:
        return jsonify({"message": "Processing error", "priority": "error"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)