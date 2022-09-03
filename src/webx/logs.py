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
mainLogger = logging.getLogger("webx")
mainLogger.setLevel(level=loglevel.get(os.getenv('env'), loglevel.get('debug')))
formatter = logging.Formatter('%(asctime)s | logger: %(name)s | line %(lineno)d  | %(funcName)s %(filename)s| %(levelname)s: %(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setLevel(level=loglevel.get(os.getenv('env'), loglevel.get('debug')))
stream_handler.setFormatter(formatter)
mainLogger.addHandler(stream_handler)

def getFileLogger(logPath):
    fileLogger = logging.getLogger("fileLogger")
    fileLogger.setLevel(logging.INFO)
    fileFormatter = logging.Formatter('%(message)s')
    file_handler = logging.FileHandler(filename=logPath)
    file_handler.setFormatter(fileFormatter)
    fileLogger.addHandler(file_handler)
    return(fileLogger)

#mainLogger.setFormatter(formatter)



''' 
CONSOLE_FORMAT = "%(levelname)s at %(asctime)s in %(funcName)s in %(filename) at line %(lineno)d: %(message)s"
FILE_FORMAT = "%(lineno)d in %(filename)s at %(asctime)s: %(message)s"

LOG_CONFIG = {'version':1,
              'formatters':{'error':{'format':CONSOLE_FORMAT},
                            'debug':{'format':CONSOLE_FORMAT}},
              'handlers':{'console':{'class':'logging.StreamHandler',
                                     'formatter':'debug',
                                     'level':logging.DEBUG},
                          'file':{'class':'logging.FileHandler',
                                  'filename':'//Users/maryam/Desktop/work/webx/webx_package_proj/some.log',
                                  'formatter':'error',
                                  'level':logging.ERROR}},
              'root':{'handlers':('console', 'file')}}

logging.config.dictConfig(LOG_CONFIG)

logger = logging.getLogger()
logger.setLevel(level=loglevel.get(os.getenv('env'), loglevel.get('debug')))

logger.error(logger)
'''