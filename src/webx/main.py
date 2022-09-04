import sys
import time
import argparse
import threading
import readConfig
import statusCheck
from datetime import datetime
from logs import getConsoleLoger, getFileLogger


def logResult(configItem, Logger):
    while True:
        _result = statusCheck.check(configItem)
        _result['url'] = configItem.get('url')
        _result['checkTime'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Logger.info(msg=_result)
        time.sleep(configItem.get('checking_frequency').get('period'))




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--logPath', required=False, type=str, default='.')
    parser.add_argument('--ConfigFilePath', required=True, type=str)
    args = parser.parse_args()
    logPath = args.logPath
    ConfigFilePath = args.ConfigFilePath
    ConfigFile = readConfig.readConfig(ConfigFilePath)
    mainLogger = getConsoleLoger('main')
    if not ConfigFile:
        mainLogger.error('ConfigFile is missing or in wrong format')
        sys.exit()
    threads = []
    for _key in ConfigFile.keys():
        fLogger = getFileLogger('./{}.txt'.format(_key), _key)
        thread = threading.Thread(target=logResult, args=(ConfigFile[_key], fLogger))
        threads.append(thread)
    for t in threads:
        t.start()

