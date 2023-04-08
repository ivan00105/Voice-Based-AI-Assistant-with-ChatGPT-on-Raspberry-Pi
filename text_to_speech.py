from gtts import gTTS
import os

def text_to_speech(text, language):
    tts = gTTS(text, lang=language)
    filename = f"output.mp3"
    tts.save(filename)
    os.system(f"start {filename}")