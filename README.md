# 🔐 Password Strength Analyzer

A modern cybersecurity-focused desktop application built with **Python** and **CustomTkinter** for analyzing password strength, identifying common weaknesses, estimating entropy, and optionally checking whether a password appears in known breach data.

---

## 📌 Project Overview

The Password Strength Analyzer demonstrates practical password-security concepts through an easy-to-use desktop interface.

Users can:

- Analyze a password in real time
- See a 0–100 strength score
- View strength classification
- Check password length and character diversity
- Detect common passwords
- Detect repeated characters
- Detect sequential characters
- Detect keyboard patterns
- Estimate password entropy
- Estimate theoretical offline cracking time
- Optionally check breach exposure using the **Have I Been Pwned Pwned Passwords API**
- Show or hide the password

The application is intentionally modular so the analysis engine can be reused independently from the graphical interface.

---

## 🚀 Features

- 🔐 Real-time password analysis
- 📊 0–100 password strength score
- 🧮 Entropy estimation
- ⏱ Offline crack-time estimate
- 🔤 Character-set analysis
- 🚫 Common-password detection
- 🔁 Repeated-character detection
- 🔢 Sequential-pattern detection
- ⌨️ Keyboard-pattern detection
- 💡 Security recommendations
- 🕵️ Optional breach lookup
- 🌙 Modern dark-themed GUI
- 🧩 Modular project architecture
- 💻 Cross-platform Python application
- 🔒 Passwords are not stored by the application

---

## 🛡️ Breach Check Privacy

The optional breach check uses the **Have I Been Pwned Pwned Passwords API** with its k-anonymity model.

The complete password is **not sent** to the service.

The application:

1. Calculates the SHA-1 hash locally.
2. Sends only the first 5 characters of that hash.
3. Receives matching hash suffixes.
4. Performs the final comparison locally.

An internet connection is required only when the breach-check feature is used.

---

## ⚠️ Important Security Note

The strength score and crack-time estimate are educational indicators, not guarantees of security.

The application does not perform real password cracking. The crack-time estimate is based on a simplified entropy model and a hypothetical offline guessing rate.

For important accounts, use a password manager and a unique password for every service.

---

## 🛠 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming |
| CustomTkinter | Modern desktop GUI |
| Tkinter | Native dialogs and GUI support |
| hashlib | Local SHA-1 hashing for breach lookup |
| urllib | HTTPS API communication |
| re | Pattern and character analysis |
| math | Entropy calculations |
| unittest | Unit testing |

---

## 📂 Project Structure

```text
Password-Strength-Analyzer/
│
├── data/
│   └── wordlists/
│       └── common_passwords.txt
│
├── src/
│   │
│   ├── app/
│   │   ├── __init__.py
│   │   └── gui.py
│   │
│   ├── analyzer/
│   │   ├── __init__.py
│   │   ├── breach.py
│   │   ├── entropy.py
│   │   ├── patterns.py
│   │   └── strength.py
│   │
│   ├── components/
│   │   ├── __init__.py
│   │   ├── header.py
│   │   ├── password.py
│   │   ├── results.py
│   │   └── strength_meter.py
│   │
│   ├── config/
│   │   ├── __init__.py
│   │   ├── paths.py
│   │   └── theme.py
│   │
│   └── main.py
│
├── tests/
│   ├── __init__.py
│   └── test_analyzer.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/aryanshrma03/Password-Strength-Analyzer.git
cd Password-Strength-Analyzer
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

From the project root:

```bash
python src/main.py
```

---

## 🧪 Run Tests

```bash
python -m unittest discover -s tests -v
```

---

## 📊 Strength Model

The analyzer evaluates several properties:

### Password Length

Longer passwords receive a higher score.

### Character Diversity

The analyzer checks for:

- Lowercase letters
- Uppercase letters
- Numbers
- Symbols

### Weak Patterns

The analyzer looks for:

- Common passwords
- Repeated characters
- Sequential characters
- Keyboard patterns

### Entropy

A rough entropy estimate is calculated from the available character pool:

```text
Entropy ≈ password length × log2(character pool size)
```

This is an estimate rather than a complete password-strength model.

---

## 🔮 Future Improvements

- [ ] Password generator
- [ ] Personal-information detection
- [ ] Larger local password dictionary
- [ ] Better linguistic pattern detection
- [ ] zxcvbn-style scoring
- [ ] Async breach checking
- [ ] Export analysis report
- [ ] Clipboard-safe password generator
- [ ] Configurable scoring profiles
- [ ] More comprehensive unit tests

---

## 👨‍💻 Author

**Aryan Sharma**

Cybersecurity-focused Python project demonstrating password security analysis and modular GUI application development.
