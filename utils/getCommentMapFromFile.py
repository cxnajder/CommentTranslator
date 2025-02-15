if __name__ == "__main__":
    from getFileParams.getFileExtension import getFileExtension
    from getFileParams.getFileEncoding import getFileEncoding
    from logger.LogError import LogError
else:
    from utils.getFileParams.getFileExtension import getFileExtension
    from utils.getFileParams.getFileEncoding import getFileEncoding
    from utils.logger.LogError import LogError
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
        LogError(f"Could not extract comments: File extension not in extensions map: {fileExtension} ({filePath})")
        return commentMap
    
    commentSign = fileExtensionToComment[fileExtension]

    fileEncoding = getFileEncoding(filePath)

    with open(filePath, 'r', encoding=fileEncoding) as file:
        for lineNumber, lineText in enumerate(file, start=0):
            lineText = lineText.strip() # remowes '\n' from the end of each line
            index = lineText.find(commentSign)
            if index == -1:
                continue
            commentText = lineText[index + len(commentSign):]
            if additionalLogic(commentText):
                commentMap[lineNumber] = commentText

    return commentMap

if __name__ == "__main__":
    # Some Tests
    print(getCommentMapFromFile('./samples/cpp/sample.cpp'))