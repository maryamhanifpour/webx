import os
import logging

loglevel = {
    'critical': logging.CRITICAL,
    'error': logging.ERROR,
    'prod': logging.WARNING,
    'dev': logging.INFO,
    'debug': logging.DEBUG
}



#logging.basicConfig()
def getConsoleLoger(name):
    mainLogger = logging.getLogger(name)
    mainLogger.setLevel(level=loglevel.get(os.getenv('env'), loglevel.get('debug')))
    formatter = logging.Formatter('%(asctime)s | logger: %(name)s | line %(lineno)d  | %(funcName)s %(filename)s| %(levelname)s: %(message)s')
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level=loglevel.get(os.getenv('env'), loglevel.get('debug')))
    stream_handler.setFormatter(formatter)
    if (mainLogger.hasHandlers()):
        mainLogger.handlers.clear()
    mainLogger.addHandler(stream_handler)
    return(mainLogger)

def getFileLogger(logPath,name):
    fileLogger = logging.getLogger(name)
    fileLogger.setLevel(logging.INFO)
    fileFormatter = logging.Formatter('%(message)s')
    file_handler = logging.FileHandler(filename=logPath)
    file_handler.setFormatter(fileFormatter)
    if (fileLogger.hasHandlers()):
        fileLogger.handlers.clear()
    fileLogger.addHandler(file_handler)
    return(fileLogger)