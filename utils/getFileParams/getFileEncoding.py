import chardet

def getFileEncoding(filePath, numBytes=0):
    with open(filePath, 'rb') as file:
        if numBytes > 0:
            rawData = file.read(numBytes)
        else:
            rawData = file.read()
        result = chardet.detect(rawData)
        encoding = result['encoding']
        # it detects utf-8 as ascii
        if encoding == 'ascii':
            encoding = 'utf-8'
        # it detects windows-1251 as MacCyrillic
        if encoding == 'MacCyrillic':
            encoding = 'windows-1251'
        return encoding

def _testGetFileEncoding(filePath, numOfBytes=0):
    encoding = getFileEncoding(filePath, numOfBytes)
    print(f'The encoding of the file \'{filePath}\' is: {encoding}')

if __name__ == "__main__":
    # Some Tests
    # To make this test work you need to run this script from project's directory like: 
    # python3 ./utils/getFileParams/getFileEncoding.py
    _testGetFileEncoding('./samples/encoding/utf-8.cpp') # utf-8
    _testGetFileEncoding('./samples/encoding/windows-1251.cpp') # windows-1251
    _testGetFileEncoding('./samples/encoding/windows-1251.cpp', 512) # windows-1251
