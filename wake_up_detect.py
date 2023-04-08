import pvporcupine
import pyaudio
import struct
import sys
import signal
from speech_to_text import recognize_speech
from text_to_speech import text_to_speech
from translator import translate
from config import porcupine_access_key
from gpt import gpt


interrupted = False

def signal_handler(signal, frame):
    global interrupted
    interrupted = True

def interrupt_callback():
    global interrupted
    return interrupted


#capture SIGINT signal, e.g. ctrl+C
signal.signal(signal.SIGINT, signal_handler)

#define the hotword model
# keyword_path = "alexa_windows.ppn" #test case with "alexa"
keyword_path = "Hey-Ras-Pi_en_raspberry-pi_v2_1_0.ppn"

#initialize the Porcupine engine
porcupine = None
try:
    porcupine = pvporcupine.create(access_key=porcupine_access_key, keyword_paths=[keyword_path])

    pa = pyaudio.PyAudio()
    audio_stream = pa.open(
                    rate=porcupine.sample_rate,
                    channels=1,
                    format=pyaudio.paInt16,
                    input=True,
                    frames_per_buffer=porcupine.frame_length)

    print("Listening for 'Hey Ras Pi'...")
    while not interrupt_callback():
        pcm = audio_stream.read(porcupine.frame_length)
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
        keyword_index = porcupine.process(pcm)
        if keyword_index >= 0:
            print("Hey Ras Pi detected! Recognizing speech...")
            query, lang = recognize_speech()
            response = gpt(query, lang)
            print(response['choices'][0]['message']["content"])
            response = response['choices'][0]['message']["content"]

            #translate to the voice input language
            if lang != "en-US":
                response = translate(response,"zh-TW")
            
            #text to speech
            if lang == "en-US":
                text_to_speech(response,"en")
            else:
                text_to_speech(response, "zh")
            
            

finally:
    if porcupine is not None:
        porcupine.delete()
    if audio_stream is not None:
        audio_stream.close()
    if pa is not None:
        pa.terminate()
