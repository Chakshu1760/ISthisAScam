# IsThisAScam

**AI-Powered Scam Detection Quiz**

_IsThisAScam_ is a cybersecurity awareness project that helps users determine whether a message might be a scam. It uses a combination of rule-based logic, NLP models, and a user-facing quiz to evaluate the risk of phishing, fraud, or scam attempts.

## 🔍 Features

- User submits a message they received (e.g., SMS, email, DM)
- AI analyzes message content using keyword scoring and basic NLP
- Short quiz asks the user about context, urgency, or suspicious elements
- Final score displays likelihood of the message being a scam
- Feedback provided with tips on common scam types

## 🚀 Tech Stack

- Python
- Flask (for web app)
- scikit-learn or OpenAI API (optional AI model)
- HTML/CSS (frontend)
- GitHub (for version control)

## 📦 Setup

```bash
git clone https://github.com/yourusername/IsThisAScam.git
cd IsThisAScam
pip install -r requirements.txt
python app.py
```

## 💡 Future Improvements

- Add scam type classification (e.g., phishing, tech support, lottery)
- Add a reporting feature for real scam messages
- Deploy as a hosted web app for public use

## 🤝 Contributions

This is a solo learning project, but collaboration is welcome. If you'd like to contribute or provide feedback, feel free to open an issue or contact me.

## 📄 License

MIT License
