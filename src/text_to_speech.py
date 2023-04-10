from gtts import gTTS
import os
import subprocess

def text_to_speech(text, language, filename="output.wav"):
    tts = gTTS(text, lang=language)
    tts.save(filename)
    subprocess.Popen(["cvlc", "--play-and-exit", "--no-repeat", filename])