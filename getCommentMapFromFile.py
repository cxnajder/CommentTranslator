from getFileExtension import getFileExtension
from getFileEncoding import getFileEncoding
from LogError import LogError
import os

fileExtensionToComment = {
    'py': '#',
    'cpp': '//',
    'h': '//',
    'hpp': '//',
    'c': '//',
    'cs': '//',
    'js': '//',
    'pas': '//',    # Pascal
    'sh': '#',      # Bash
    'rb': '#',      # Ruby
    'pl': '#',      # Perl
    'pro': '%',     # Prolog
    'hs': '--',     # Haskell
    'ada': '--',    # ADA
    'ads': '--',    # -||-
    'vhd': '--',    # VHDL
    'vhdl': '--',   # -||-
    'asm': ';',     # Assemply
    'm': '%',       # Matlab
}

def defaultLogic(arg):
    return True

def getCommentMapFromFile(filePath, additionalLogic=defaultLogic):
    commentMap = {}
    fileName = os.path.basename(filePath)
    fileExtension = getFileExtension(fileName)

    if fileExtension not in fileExtensionToComment:
        LogError(f"File extension not in extensions map: {fileExtension} ({filePath})")
        return commentMap
    
    commentSign = fileExtensionToComment[fileExtension]

    fileEncoding = getFileEncoding(filePath)

    with open(filePath, 'r', encoding=fileEncoding) as file:
        for lineNumber, lineText in enumerate(file, start=1):
            lineText = lineText.strip() # remowes '\n' from the end of each line
            index = lineText.find(commentSign)
            if index == -1:
                continue
            commentText = lineText[index + len(commentSign):]
            if additionalLogic(commentText):
                commentMap[index] = commentText

    return commentMap

if __name__ == "__main__":
    # Some Tests
    print(getCommentMapFromFile('./samples/cpp/sample.cpp'))