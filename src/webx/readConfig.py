import json
from logs import mainLogger

def readConfig(path):
    try:
        with open(path, 'r') as f:
            webConfigFile = json.load(f)
    except Exception as e:
        mainLogger.error(e)
        webConfigFile=None
    # todo: check schema of config file
    return(webConfigFile)