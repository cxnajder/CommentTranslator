import os
from checkTextForForeingLang import checkTextForForeingLang
from translateText import translateText

def translateFile(filePath):
    commentMap = getCommentMapFromFile(filePath, checkTextForForeingLang)

    # open file and get content

    for key, value in my_dict.items():
        commentMap[key] = translateText(value)
        # replace comments in content

    # replace file content


def translateFiles(folderPath):
     for root, _, files in os.walk(folderPath):
        for fileName in files:
            filePath = os.path.join(root, fileName)
            translateFile(filePath)