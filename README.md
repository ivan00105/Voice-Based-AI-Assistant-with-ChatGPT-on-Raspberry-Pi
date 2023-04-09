# Voice-Based-AI-Assistant-with-ChatGPT-on-Raspberry-Pi
This project is an implementation of a voice-based AI assistant using OpenAI's ChatGPT and Bing on a Raspberry Pi. The assistant listens for the wake word "Hey Ras Pi" and then processes the user's query, providing an appropriate response. The project demonstrates how to integrate multiple language models and APIs to create a more robust AI assistant.

## Features
- Wake word detection using Porcupine
- Speech recognition with Google Speech Recognition
- AI-based chat using ChatGPT and Bing APIs
- Multilingual support for English, Mandarin, and Cantonese
- Text-to-Speech using Google Text-to-Speech (gTTS)

## Installation
1. Clone the repository
```bash
git clone https://github.com/yourusername/Voice-Based-AI-Assistant-with-ChatGPT-on-Raspberry-Pi.git
cd Voice-Based-AI-Assistant-with-ChatGPT-on-Raspberry-Pi
```
2. Update and install your Raspberry Pi packages:
```bash
sudo apt-get update
sudo apt-get upgrade
chmod +x install_dependencies.sh
./install_dependencies.sh
```
3. Set up a virtual environment and activate it
```bash
python3 -m venv env
#on Pi
source env/bin/activate
#on Windows
./env/bin/activate
```
4. Install the required packages
```bash
pip install -r requirements.txt
```

## Usage
1. Run the main script:
```bash
python main.py
```
2. The assistant will listen for the wake word "Hey Ras Pi". Once detected, it will prompt you to speak your query.

3. The assistant will process your query using ChatGPT and Bing APIs and provide an appropriate response.

## Directory Structure
```bash
.
├── ./.gitignore
├── ./README.md
├── ./cookies.json
├── ./env
├── ./install_dependencies.sh
├── ./main.py
├── ./models
│   ├── ./models/Hey-Ras-Pi_en_raspberry-pi_v2_1_0.ppn
│   ├── ./models/Hey-Ras-Pi_en_raspberry-pi_v2_1_0.zip
│   └── ./models/alexa_windows.ppn
├── ./output.mp3
├── ./requirements.txt
└── ./src
    ├── ./src/__pycache__
    ├── ./src/bing.py
    ├── ./src/config.py
    ├── ./src/config_example.py
    ├── ./src/gpt.py
    ├── ./src/speech_to_text.py
    ├── ./src/text_to_speech.py
    ├── ./src/translator.py
    └── ./src/wake_up_detect.py
```
