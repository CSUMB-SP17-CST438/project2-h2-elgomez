#parses messages and inserts html tags if necessary.
import validators
def checkURL(message):
    b = validators.url(message)
    return b
    
def isImage(message):
    if(message[-4:] == ".jpg"):
        return True
    elif(message[-4:] == ".gif"):
        return True
    elif(message[-4:] == ".png"):
        return True
    elif(message[-5:] == ".jpeg"):
        return True
    else:
        return False