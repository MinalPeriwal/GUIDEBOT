<<<<<<< HEAD
# GUIDEBOT
GUIDEBOT is a Streamlit-based rule-driven chatbot that answers traffic and road-safety questions in real time. It offers quick guidance on signals, signs, and driving rules through a clean web interface—no AI or ML required.
=======
# GUIDEBOT - Streamlit Chatbot Web App

A secure, modern chatbot web application built with Streamlit featuring user authentication and a clean conversational interface.

## Features

- 🔐 **Secure Authentication**: Login/register system with hashed passwords
- 💬 **Chat Interface**: Clean, responsive conversation UI
- 🤖 **Modular Chatbot**: Easy to replace with LLM APIs
- 📱 **Responsive Design**: Works on desktop and mobile
- 🗄️ **SQLite Database**: Secure credential storage

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
streamlit run app.py
```

3. Open your browser to `http://localhost:8501`

## Usage

1. **Register**: Create a new account with username, email, and password
2. **Login**: Access the chatbot with your credentials
3. **Chat**: Start conversing with GUIDEBOT
4. **Logout**: Securely end your session

## File Structure

- `app.py` - Main Streamlit application
- `auth.py` - Authentication logic
- `database.py` - Database operations and password hashing
- `chatbot.py` - Chatbot response logic (easily replaceable)
- `requirements.txt` - Python dependencies

## Customization

To integrate with an LLM API (OpenAI, etc.), simply modify the `get_response()` method in `chatbot.py`.

## Security

- Passwords are hashed using bcrypt
- SQLite database for secure local storage
- Session-based authentication
>>>>>>> 76afb0b (Initial commit)
