import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Please speak...")
        audio = recognizer.listen(source)

    try:
        #recognition in English, Mandarin, Cantonese
        languages = ["en-US", "zh-CN", "yue-Hant-HK" ]
        results = []
        print("Recognizing...")
        for language in languages:
            result = recognizer.recognize_google(audio, language=language, show_all=True)
            if 'alternative' in result:
                for alt in result['alternative']:
                    if 'confidence' in alt:
                        results.append((alt['transcript'], alt['confidence'], language))

        #find the most confident result
        best_result = max(results, key=lambda x: x[1])
        print(best_result)
        print(f"You said: {best_result[0]} (Language: {best_result[2]})")
        return [best_result[0], best_result[2]]

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError as e:
        print(f"Error: {e}")

