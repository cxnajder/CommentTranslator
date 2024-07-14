from googletrans import Translator
from logger.LogError import LogError

def translateText(text, destinationLanguage='en'):
    translator = Translator()
    try:
        translation = translator.translate(text, dest=destinationLanguage)
    except Exception as e:
        LogError(f'Translation of \'{text}\' failed: \'{e}\'; Returning original text.')
        return text
    return translation.text

if __name__ == "__main__":
    # Test cases
    print(translateText("Привет, мир!"))
    print(translateText("Hola, mundo!"))
    print(translateText("Bonjour le monde!"))
