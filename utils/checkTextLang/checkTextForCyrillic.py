import re

def checkTextForCyrillic(text):
    # Define the regex pattern for Cyrillic characters
    cyrillicPattern = re.compile(r'[\u0400-\u04FF]')
    
    # Search for the pattern in the text
    if cyrillicPattern.search(text):
        return True
    return False


if __name__ == "__main__":
    # Test cases
    print(checkTextForCyrillic("Hello, world!"))
    print(checkTextForCyrillic("Привет, мир!"))
    print(checkTextForCyrillic("Hello, мир!"))