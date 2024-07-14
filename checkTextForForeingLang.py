from langdetect import detect, DetectorFactory
from langdetect import detect_langs as detectLangs
from langdetect.lang_detect_exception import LangDetectException

DetectorFactory.seed = 0

def checkTextForForeingLang(text, targetLanguage='en'):
    try:
        # Detect the dominant language in the text
        detectedLanguages = detectLangs(text)
        
        for lang in detectedLanguages:
            if lang.lang != targetLanguage:
                return True
        
        return False
    
    except LangDetectException:
        return False

if __name__ == "__main__":
    # Test cases
    print(checkTextForForeingLang("Hello, world!"))
    print(checkTextForForeingLang("Привет, мир!"))
    print(checkTextForForeingLang("Hello, мир!"))