import os
import logging
import requests

loglevel = {
    'critical': logging.CRITICAL,
    'error': logging.ERROR,
    'prod': logging.INFO,
    'dev': logging.INFO,
    'debug': logging.DEBUG
}
logger = logging.getLogger()
logger.setLevel(level=loglevel.get(os.getenv('env'), loglevel.get('debug')))


url = ""
payload = {}
headers = {}
method = "GET"

response = requests.request(method, url, headers=headers)


print(response)