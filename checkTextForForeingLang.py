from langdetect import detect, DetectorFactory
from langdetect import detect_langs as detectLangs
from langdetect.lang_detect_exception import LangDetectException

DetectorFactory.seed = 0

def containsForeignLanguage(text, targetLanguage='en'):
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
    print(containsForeignLanguage("Hello, world!"))
    print(containsForeignLanguage("Привет, мир!"))
    print(containsForeignLanguage("Hello, мир!"))