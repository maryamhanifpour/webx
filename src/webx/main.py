import sys
import time
import argparse
import readConfig
import statusCheck
from datetime import datetime
from logs import mainLogger, getFileLogger




def logResult(configItem, _key):
    fileLogger = getFileLogger('./{}.txt'.format(_key))
    while True:
        _result = statusCheck.check(configItem)
        _result['url'] = configItem.get('url')
        _result['checkTime'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        fileLogger.info(msg=_result)
        mainLogger.info('sleeping')
        # todo: convert period to seconds
        time.sleep(configItem.get('checking_frequency').get('period'))






if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--logPath', required=False, type=str, default='.')
    parser.add_argument('--ConfigFilePath', required=True, type=str)
    args = parser.parse_args()
    logPath = args.logPath
    ConfigFilePath = args.ConfigFilePath
    ConfigFile = readConfig.readConfig(ConfigFilePath)
    if ConfigFile:
        mainLogger.info(ConfigFile)  
    else:
        mainLogger.error('ConfigFile is missing or in wrong format')
        sys.exit()
    # todo: map items to threads
    _key = 'elastic'
    configItem = ConfigFile[_key]
    logResult(configItem, _key)


