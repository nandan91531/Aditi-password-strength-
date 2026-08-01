# 🛡️ PassShield - Python Password Strength Checker & Generator

An advanced, feature-packed Password Strength Evaluator and Secure Generator built with **Python**. Evaluates password security across key metrics including length, character sets (uppercase, lowercase, numbers, special characters), pattern/dictionary weakness detection, and estimated brute-force crack time.

Includes both a **Terminal CLI** and a **Web Dashboard UI (Flask)**.

---

## 🌟 Key Features

1. **Multi-Criteria Analysis**:
   - 📏 **Length**: Evaluates short (<8), standard (8-11), strong (12-15), and ultra-secure (16+) lengths.
   - 🔠 **Uppercase Letters**: Checks presence and count of `[A-Z]`.
   - 🔡 **Lowercase Letters**: Checks presence and count of `[a-z]`.
   - 🔢 **Digits**: Checks presence and count of `[0-9]`.
   - 🔣 **Special Symbols**: Checks count and variety of characters like `!@#$%^&*()`.

2. **Pattern & Weakness Detection**:
   - Flags common dictionary passwords (`password`, `admin`, `123456`).
   - Identifies sequential character/number patterns (`1234`, `abcd`).
   - Detects repeating identical characters (`aaaaa`).

3. **Brute-Force Crack Time Estimation**:
   - Calculates estimated time required for high-speed offline GPU brute-force attacks (ranging from *Instant* to *Millions of Years*).

4. **Cryptographically Secure Generator**:
   - Generates customizable passwords using Python's `secrets` module.
   - Guarantees character set inclusion rules.

5. **Dual Interface**:
   - 🌐 **Interactive Web UI**: Real-time evaluation, glassmorphism dark mode, animated gauge meter, breakdown cards, one-click copy.
   - 💻 **Terminal CLI**: Colorized terminal output, hidden password prompt, and command line flags.

---

## 🚀 Quick Start

### 1. Installation

Install dependencies (Flask):
```bash
pip install -r requirements.txt
```

### 2. Running the Web UI

Launch the Flask app server:
```bash
python app.py
```
Open your browser at `http://127.0.0.1:5000`.

### 3. Running the Terminal CLI

Interactive mode:
```bash
python main.py
```

Evaluate a specific password:
```bash
python cli.py -p "K9#mQ2$xP8!vL5@w"
```

Generate a random strong password (default 16 chars):
```bash
python cli.py -g -l 20
```

### 4. Running Unit Tests

Run the automated test suite:
```bash
python -m unittest discover tests
```

---

## 📁 Project Structure

```
password-strength-checker/
├── checker/
│   ├── __init__.py
│   ├── strength_evaluator.py  # Main evaluation engine
│   └── generator.py           # Secure password generator
├── templates/
│   └── index.html             # Flask Web UI Template
├── static/
│   ├── css/
│   │   └── style.css          # Glassmorphism dark mode styling
│   └── js/
│       └── app.js             # Real-time frontend interaction
├── tests/
│   ├── __init__.py
│   └── test_evaluator.py      # Automated unit tests
├── app.py                     # Flask web app server
├── cli.py                     # Command line interface
├── main.py                    # Quick CLI launcher
├── requirements.txt           # Project dependencies
└── README.md                  # Documentation
```
