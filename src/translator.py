from googletrans import Translator

def translate(text,lang):
    translator = Translator()
    translated = translator.translate(text, dest=lang)
    return translated.text