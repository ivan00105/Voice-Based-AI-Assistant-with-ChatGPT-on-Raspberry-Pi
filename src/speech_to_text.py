import threading
import speech_recognition as sr

recognizer = sr.Recognizer()

#thread for recognize_google()
def recognize_google_thread(audio, language, results):
    try:
        result = recognizer.recognize_google(audio, language=language, show_all=True)
        if 'alternative' in result:
            for alt in result['alternative']:
                if 'confidence' in alt:
                    results.append((alt['transcript'], alt['confidence'], language))
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print(f"Error: {e}")

def recognize_speech():
    with sr.Microphone() as source:
        print("Please speak...")
        audio = recognizer.listen(source)
    # English, Mandarin, Cantonese
    languages = ["en-US", "zh-CN", "yue-Hant-HK"]
    results = []

    #multithreading the recognition in different languages
    threads = []
    for language in languages:
        t = threading.Thread(target=recognize_google_thread, args=(audio, language, results))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    #process the results
    if results:
        #return the language with the highest confidence value based on x[1]
        best_result = max(results, key=lambda x: x[1])
        print(best_result)
        print(f"You said: {best_result[0]} (Language: {best_result[2]})")
        return [best_result[0], best_result[2]]
    else:
        print("Sorry, I couldn't understand what you said.")
        return [None, None]