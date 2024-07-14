import os
from getFileEncoding import getFileEncoding
import LogError

_extensionsCommentsMapInline = {
    'py': '#',
    'cpp': '//',
    'h': '//',
    'hpp': '//',
    'c': '//',
    'cs': '//',
    'js': '//',
    'pas': '//',
}


def _getFirstFileExtension(fileName):
    '''
    Expectation:
    "main.py" => "py"
    "config.h.in" => "h"
    "text" => ""
    '''
    parts = fileName.split('.')
    if len(parts) > 1:
        return parts[1]
    else:
        return ''

def __testGetFirstFileExtension(fileName):
    return f"{fileName} => {_getFirstFileExtension(fileName)}"

def runTestsGetFirstFileExtension():
    print(subtitleDecorator("Testing _getFirstFileExtension(fileName):"))
    print(testDecoraotr(__testGetFirstFileExtension("main.py"))) # py
    print(testDecoraotr(__testGetFirstFileExtension("config.h.in"))) # h
    print(testDecoraotr(__testGetFirstFileExtension("text"))) # (empty)

def testDecoraotr(str):
    return f"> {str}"

def subtitleDecorator(str):
    return f"| {str}"

def performFuncOnCommentInline(folderPath, func, extensionsCommentsMap):
    for root, _, files in os.walk(folderPath):
        for fileName in files:
            fileExtension = _getFirstFileExtension(fileName)
            if fileExtension not in extensionsCommentsMap:
                LogError(f"File extension not in extensions map: {fileName} in {root}")
                continue
            commentIndicator = extensionsCommentsMap[fileExtension]
            filePath = os.path.join(root, fileName)
            fileEncoding = getFileEncoding(filePath)
            with open(filePath, 'r', encoding=fileEncoding) as file:
                for lineNumber, line in enumerate(file, start=1):
                    strippedLine = line.strip()
                    index = strippedLine.find(commentIndicator)
                    if index == -1:
                        continue
                    commentContent = strippedLine[index + len(commentIndicator):].strip()
                    func(commentContent, filePath, lineNumber)


def __tetsFuncForPerformFuncOnCommentInline(commentContent, filePath, lineNumber):
    return f"{filePath}#L{lineNumber}:{commentContent};"

def _tetsFuncPrintForPerformFuncOnCommentInline(commentContent, filePath, lineNumber):
    print(testDecoraotr(__tetsFuncForPerformFuncOnCommentInline(commentContent, filePath, lineNumber)))

def runTestPerformFuncOnCommentInline():
    samplesFolderPath = "./samples"
    testedFunc = _tetsFuncPrintForPerformFuncOnCommentInline

    print(subtitleDecorator("Testing performFuncOnCommentInline(folderPath, func, extensionsCommentsMap):"))
    performFuncOnCommentInline(samplesFolderPath, testedFunc, _extensionsCommentsMapInline)

if __name__ == "__main__":
    # Some Tests
    print("Script run as __main__")
    print("Starting tests:")
    runTestsGetFirstFileExtension()
    runTestPerformFuncOnCommentInline()
