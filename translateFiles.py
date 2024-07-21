import os
import re
from utils.checkTextLang.checkTextForForeignLang import checkTextForForeignLang
from utils.checkTextLang.checkTextForCyrillic import checkTextForCyrillic
from utils.translateText import translateText
from utils.getCommentMapFromFile import getCommentMapFromFile, fileExtensionToComment
from utils.getFileParams.getFileExtension import getFileExtension
from utils.getFileParams.getFileEncoding import getFileEncoding
from utils.logger.LogError import LogError


def translateFiles(folderPath):
     for root, _, files in os.walk(folderPath):
        for fileName in files:
            filePath = os.path.join(root, fileName)
            translateFile(filePath)


def translateFile(filePath):
    # replace 'checkTextForForeignLang' with 'checkTextForCyrillic' if you are interested only in translating cyrillic
    translateCondition = checkTextForForeignLang
    commentMap = getCommentMapFromFile(filePath, translateCondition)

    for lineNum, comment in commentMap.items():
        commentMap[lineNum] = translateText(comment)
 
    replaceCommentsInFile(filePath, commentMap)

   
def replaceCommentsInFile(filePath, commentMap):

    fileExt = getFileExtension(os.path.basename(filePath))
    if fileExt not in fileExtensionToComment:
        LogError(f"Could not translate: File extension not in extensions map: {fileExt} ({filePath})")
        return
    commentPattern = fileExtensionToComment[fileExt]

    fileEncoding = getFileEncoding(filePath)
    with open(filePath, 'r', encoding=fileEncoding) as file:
        fileLines = file.readlines()

        for lineNum, comment in commentMap.items():
            fileLines[lineNum] = replaceCommentInLine(fileLines[lineNum], comment, commentPattern)

    with open(filePath, 'w', encoding='utf-8') as file:
        file.writelines(fileLines)



def replaceCommentInLine(line, newComment, commentPattern):
    index = line.index(commentPattern)
    newLine = line[:index + len(commentPattern)] + ' ' +newComment
    if line.endswith('\n'):
        newLine += '\n'
    return newLine

if __name__ == "__main__":
    folderPathToTranslate = './samples'
    translateFiles(folderPathToTranslate)