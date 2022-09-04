import json
from webx.logs import getConsoleLoger

mainLogger = getConsoleLoger('readConfig')

def readConfig(path):
    try:
        with open(path, 'r') as f:
            webConfigFile = json.load(f)
    except Exception as e:
        mainLogger.error(e)
        webConfigFile=None
    # todo: check schema of config file
    # todo: convert frequency unit to seconds
    return(webConfigFile)