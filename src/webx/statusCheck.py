from os import stat
import requests
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError
from webx.logs import getConsoleLoger

checkLogger = getConsoleLoger('statusCheck')

def checkTags(soup, item):
    _check = soup.find_all(item.get('tag'), text=item.get('text'))
    _state ='pass' if len(_check) > 0  else 'fail'
    item['state'] = _state
    return(item)

def check(configItem):
    url = configItem.get('url')
    method = configItem.get('method')
    headers = configItem.get('headers')
    tags = configItem.get('tags')
    expected_response = configItem.get('expected_response').get('status_code')
    try:
        response = requests.request(method=method, url=url, headers=headers)
    except ConnectionError:
        reachablity = 'fail'
        responseTagCheck = []
        responseCodeCheck = None
        responseTimeMilSec = None
    except Exception as e:
        checkLogger.error(e)
    else:  
        reachablity = 'pass'
        soup = BeautifulSoup(response.text, 'html.parser')
        if len(tags) > 0:
            responseTagCheck = list(map(lambda i:checkTags(soup, tags[i]), range(0, len(tags))))
        else:
            responseTagCheck = []
        responseCodeCheck = 'pass' if response.status_code == expected_response else 'fail'
        responseTimeMilSec = response.elapsed.microseconds/1000
    finally:
        _result = {}
        _result['reachablity'] = reachablity
        _result['responseTagCheck'] = responseTagCheck
        _result['responseCodeCheck'] = responseCodeCheck
        _result['responseTimeMilSec'] = responseTimeMilSec
    return(_result)
