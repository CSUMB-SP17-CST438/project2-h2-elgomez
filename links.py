#parses messages and inserts html tags if necessary.
import validators
def checkURL(message):
    b = validators.url(message)
    return b
    
def isImage(message):
    if(message[-4:] == ".jpg"):
        return True
    else:
        return False