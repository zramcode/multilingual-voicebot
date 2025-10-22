AI-powered Multilingual Voice Assistant / Voicebot
🔹 Description

This project is a Voicebot that allows users to upload audio files and receive intelligent spoken responses. The bot:

Converts speech-to-text from user audio

Detects the language and translates content as needed

Refines the transcript to fix grammar and technical errors

Runs moderation to ensure safe content

Generates AI responses using OpenAI GPT-4o

Converts the response back to speech for the user

⚠️ The project is currently in development and actively being improved.

🔹 Features

Speech-to-Text: Converts user audio into text

Translation: Supports multilingual input and output

Text Refinement: Corrects transcription and grammar errors

Moderation: Ensures content is safe and appropriate

Voicebot: Generates AI responses and converts them to audio

FastAPI & OOP Design: Modular, scalable, and clean architecture

🔹 Tech Stack

Python 3.10+

FastAPI
 (Web server)

OpenAI GPT-4o
 (Speech & text AI)

Modular OOP structure for maintainability


# Create a virtual environment
python -m venv venv
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Start the FastAPI server
uvicorn app:app --reload
