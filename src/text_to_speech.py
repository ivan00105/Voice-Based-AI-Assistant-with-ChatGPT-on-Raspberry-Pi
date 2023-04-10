from gtts import gTTS
import os

def text_to_speech(text, language):
    tts = gTTS(text, lang=language)
    filename = f"output.wav"
    tts.save(filename)
    os.system(f"aplay {filename}")