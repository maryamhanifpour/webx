import sys
import argparse
import readConfig
import statusCheck
import schedule
import threading
from datetime import datetime
from logs import mainLogger, getFileLogger


_lock = threading.Lock()

def f(configItem, _key):
    schedule.every(configItem.get('checking_frequency').get('period')).seconds.do(logResult, configItem, _key)

    while True:
        _lock.acquire()
        schedule.run_pending()
        _lock.release()

def logResult(configItem, _key):
    print(_key, datetime.now(), "I'm running on thread %s" % threading.current_thread())
    fileLogger = getFileLogger('./{}.txt'.format(_key))
    _result = statusCheck.check(configItem)
    _result['url'] = configItem.get('url')
    _result['checkTime'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    fileLogger.info(msg=_result)




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--logPath', required=False, type=str, default='.')
    parser.add_argument('--ConfigFilePath', required=True, type=str)
    args = parser.parse_args()
    logPath = args.logPath
    ConfigFilePath = args.ConfigFilePath
    ConfigFile = readConfig.readConfig(ConfigFilePath)
    if not ConfigFile:
        mainLogger.error('ConfigFile is missing or in wrong format')
        sys.exit()
    # todo: map items to threads
    threads = []
    for _key in ConfigFile.keys():
        thread = threading.Thread(target=f, args=(ConfigFile[_key], _key))
        threads.append(thread)
    for t in threads:
        t.start()
