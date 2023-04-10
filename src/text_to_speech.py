from gtts import gTTS
from playsound import playsound

def text_to_speech(text, language):
    tts = gTTS(text, lang=language)
    filename = "output.wav"
    tts.save(filename)
    playsound(filename)