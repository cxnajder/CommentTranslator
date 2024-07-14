from googletrans import Translator

def translateText(text, destinationLanguage='en'):
    translator = Translator()
    try:
        translation = translator.translate(text, dest=destinationLanguage)
    except Exception as e:
        # Maybe log some error here, idk...
        print(f'Translation of {text} failed: {e}; Returning original text.')
        return text
    return translation.text

if __name__ == "__main__":
    # Test cases
    print(translateText("Привет, мир!"))
    print(translateText("Hola, mundo!"))
    print(translateText("Bonjour le monde!"))
