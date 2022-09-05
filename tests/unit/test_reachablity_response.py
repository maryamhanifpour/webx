import sys
sys.path.append('.')
import pytest
from src.webx import statusCheck


reachable_items = [{'url': 'https://stackoverflow.com', 'method': 'post', 'expected_response': {'status_code': 200}},
         {'url': 'https://www.google.com', 'method': 'get', 'expected_response': {'status_code': 200}}]

not_reachable_items = [{'url': 'https://d4a0027q59.execute-api.eu-central-1.amazonaws.com/v1/hello', 'method': 'post', 'expected_response': {'status_code': 200}}]



@pytest.mark.parametrize("item", reachable_items)
def test_reachability_response(item):
    res = statusCheck.check(item)   
    assert res.get('reachablity') == 'pass'


@pytest.mark.parametrize("item", not_reachable_items)
def test_not_reachability_response(item):
    res = statusCheck.check(item)   
    assert res.get('reachablity') == 'fail'
