import logging

def createLoggerObj(): 
    fileName  = 'sqaProject.log' 
    formatStr = '%(asctime)s %(message)s'
    logging.basicConfig(format=formatStr, filename=fileName, level=logging.INFO)
    myLogObj = logging.getLogger('sqa2023-logger') 
    return myLogObj