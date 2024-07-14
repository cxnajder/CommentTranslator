import os
from utils.checkTextLang.checkTextForForeignLang import checkTextForForeignLang
from utils.checkTextLang.checkTextForCyrillic import checkTextForCyrillic
from utils.translateText import translateText
from utils.getCommentMapFromFile import getCommentMapFromFile

def translateFile(filePath):
    # replace 'checkTextForForeignLang' with 'checkTextForCyrillic' if you are interested only in translating cyrillic
    commentMap = getCommentMapFromFile(filePath, checkTextForForeignLang)

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