import chardet

def getFileEncoding(filePath, numBytes=512):
    with open(filePath, 'rb') as file:
        rawData = file.read(numBytes)
        result = chardet.detect(rawData)
        encoding = result['encoding']
        if encoding == 'ascii':
            encoding = 'utf-8'
        return encoding

def _testGetFileEncoding(filePath):
    encoding = getFileEncoding(filePath)
    print(f'The encoding of the file \'{filePath}\' is: {encoding}')

if __name__ == "__main__":
    # Some Tests
    _testGetFileEncoding('./samples/encoding/utf-8.cpp') # utf-8
    _testGetFileEncoding('./samples/encoding/windows-1251.cpp') # windows-1251
