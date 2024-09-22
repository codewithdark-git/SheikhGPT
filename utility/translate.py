from deep_translator import GoogleTranslator




# Language settings
LANGUAGES = {
    "English": {"code": "en", "voice": "en-US-GuyNeural"},
    "Arabic": {"code": "ar", "voice": "ar-SA-HamedNeural"},
    "Urdu": {"code": "ur", "voice": "ur-PK-AsadNeural"},
    "Indonesian": {"code": "id", "voice": "id-ID-ArdiNeural"},
    "French": {"code": "fr", "voice": "fr-FR-HenriNeural"},
    "Spanish": {"code": "es", "voice": "es-ES-AlvaroNeural"},
    "Turkish": {"code": "tr", "voice": "tr-TR-AhmetNeural"},
    "Malay": {"code": "ms", "voice": "ms-MY-OsmanNeural"}
}

# Translate text
def translate_text(text, src_lang, dest_lang):
    if src_lang == dest_lang:
        return text
    translator = GoogleTranslator(source=LANGUAGES[src_lang]['code'], target=LANGUAGES[dest_lang]['code'])
    return translator.translate(text)
