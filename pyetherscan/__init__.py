"""Python API for using etherscan.io."""
import requests
from .tokens import tokens

BASE_URL = 'https://api.etherscan.io/api?'

def get_balance(address, token=None, api_key=None):
    req_url = BASE_URL + 'module=account&tag=latest&address=%s' % address
    if not token:
        req_url += '&action=balance'
    else:
        if len(token) < 10:
            try:
                token = next(item for item in tokens if item["symbol"] == token.upper())['address']
            except StopIteration:
                return False
        req_url += '&action=tokenbalance&contractaddress=%s' % token
    if api_key: req_url += '&apikey=' + api_key
    try:
        response = requests.get(req_url).json()
    except ConnectionError:
        return False
    if response.get('status'):
        if response.get('status') == '1':
            return int(response['result']) / (10**18)
    return False
