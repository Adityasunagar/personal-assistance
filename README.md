# personal-assistance
Aizen is a Python-based personal voice assistant that can perform various tasks such as searching Wikipedia, playing music, opening websites, telling jokes, detecting user emotions, system monitoring, sending emails, and more — all through voice commands.

# Aizen - Personal Voice Assistant 🧠🎙️

Aizen is a Python-based voice assistant capable of performing a variety of tasks through simple voice commands. It can greet users, search Wikipedia, tell jokes, play music, report system status, and more.

## Features

- 📚 Wikipedia Search
- 🎵 Music Playback
- 📆 Time and Date Reporting
- 🌐 Website Opening (YouTube, Google, StackOverflow, etc.)
- 🤖 Emotion Detection (via TextBlob)
- 💻 System Status (CPU & Battery)
- 😂 Tells Jokes (via pyjokes)
- 📩 Email Sending (basic functionality)
- 🗣️ Voice Recognition (Google Speech API)
- 📝 Set Reminders
- ⚙️ Open VS Code or other programs

## Setup

1. Clone the repository:



2. Install the dependencies:


3. Run the assistant:

## Note

- Works best with a microphone and stable internet for voice recognition.
- Customize paths like music directory and VS Code location to suit your system.

## License

[MIT](LICENSE)


python, voice-assistant, speech-recognition, pyttsx3, personal-assistant, automation, AI, voice-control, desktop-assistant

📂 Suggested Folder Structure:

Aizen-Voice-Assistant/
│
├── Aizen.py                  # Main assistant script
├── README.md                 # Project documentation
├── requirements.txt          # All dependencies
├── assets/                   # Optional: Icons, audio samples, etc.
└── LICENSE                   # Recommended: Add an open-source license (MIT or GPL)


📦 requirements.txt (Recommended content):
pyttsx3
speechrecognition
wikipedia
pyjokes
psutil
textblob
requests

To generate it automatically (if you've installed all packages in your environment), you can run:
pip freeze > requirements.txt

