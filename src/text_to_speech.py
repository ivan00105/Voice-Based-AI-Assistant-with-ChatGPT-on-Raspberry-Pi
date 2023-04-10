from gtts import gTTS
import os

def text_to_speech(text, language, filename="output.wav"):
    tts = gTTS(text, lang=language)
    tts.save(filename)
    os.system(f"vlc --play-and-exit --no-repeat {filename}")