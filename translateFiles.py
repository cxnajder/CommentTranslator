import os
import re
from utils.checkTextLang.checkTextForForeignLang import checkTextForForeignLang
from utils.checkTextLang.checkTextForCyrillic import checkTextForCyrillic
from utils.translateText import translateText
from utils.getCommentMapFromFile import getCommentMapFromFile, fileExtensionToComment
from utils.getFileParams.getFileExtension import getFileExtension
from utils.getFileParams.getFileEncoding import getFileEncoding
from utils.logger.LogError import LogError


def translateFiles(folderPath, userPermissionRequired=False):
     for root, _, files in os.walk(folderPath):
        for fileName in files:
            filePath = os.path.join(root, fileName)
            translateFile(filePath, userPermissionRequired)


def translateFile(filePath, userPermissionRequired=False):
    # replace 'checkTextForForeignLang' with 'checkTextForCyrillic' if you are interested only in translating cyrillic
    translateCondition = checkTextForForeignLang
    commentMap = getCommentMapFromFile(filePath, translateCondition)

    linesToRemove = []
    
    for lineNum, comment in commentMap.items():
        if not userPermissionRequired:
            commentMap[lineNum] = translateText(comment)
        elif askUserPermission(comment):
            commentMap[lineNum] = translateText(comment)
        else:
            # If user denied of translation add line number to removal
            linesToRemove.append(lineNum)

    # Remove denied lines
    for lineNum in linesToRemove:
        del commentMap[lineNum]

    replaceCommentsInFile(filePath, commentMap)


def askUserPermission(textToTranslate):
    print(f"Woud you like to translate:\n {textToTranslate}")
    _input = input(">")
    confirmation = ["y", "Y", "yes", "Yes", "YES"]
    if _input in confirmation:
        return True
    else:
        return False
   
def replaceCommentsInFile(filePath, commentMap):

    if commentMap == {}: # empty dict
        return

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
    
    # This space before comment is important since googletranslate api 
    # removes first white space from translated text:
    # " text" => "text (but translated)"

    # (I assumed most of commants have a space in front. personally I prefer this format)

    if line.endswith('\n'):
        newLine += '\n'
    return newLine

if __name__ == "__main__":
    folderPathToTranslate = './samples'
    translateFiles(folderPathToTranslate, userPermissionRequired=True)