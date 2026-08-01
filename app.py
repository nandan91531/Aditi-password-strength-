import sys
import os

# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import io
import re
from flask import Flask, render_template, request, jsonify, send_file
from gtts import gTTS
from checker.strength_evaluator import PasswordEvaluator
from checker.generator import PasswordGenerator

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/evaluate", methods=["POST"])
def evaluate_api():
    data = request.get_json() or {}
    password = data.get("password", "")
    result = PasswordEvaluator.evaluate(password)
    return jsonify(result)

@app.route("/api/generate", methods=["POST"])
def generate_api():
    data = request.get_json() or {}
    length = int(data.get("length", 16))
    use_uppercase = bool(data.get("uppercase", True))
    use_lowercase = bool(data.get("lowercase", True))
    use_digits = bool(data.get("digits", True))
    use_special = bool(data.get("special", True))

    generated_password = PasswordGenerator.generate(
        length=length,
        use_uppercase=use_uppercase,
        use_lowercase=use_lowercase,
        use_digits=use_digits,
        use_special=use_special
    )

    evaluation = PasswordEvaluator.evaluate(generated_password)

    return jsonify({
        "password": generated_password,
        "evaluation": evaluation
    })

@app.route("/api/tts")
def tts_api():
    text = request.args.get("text", "")
    # Clean text of emojis & symbols
    clean_text = re.sub(r'[\u2600-\u27BF\u1F300-\u1FAFF]', '', text).strip()
    if not clean_text:
        clean_text = "Namaste bestie!"

    try:
        # Use gTTS with soft female accent (tld='co.uk')
        tts = gTTS(text=clean_text, lang='en', tld='co.uk', slow=False)
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        return send_file(fp, mimetype="audio/mpeg")
    except Exception as e:
        print("TTS generation error:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print("Starting AditiPassChecker Web Server on http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
