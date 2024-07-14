def getFileExtension(fileName):
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