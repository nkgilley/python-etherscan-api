"""Python API for using etherscan.io."""
import requests

BASE_URL = 'https://api.etherscan.io/api?'

def get_balance(address, api_key=None):
    req_url = BASE_URL + 'module=account&action=balance&tag=latest&address=' + address
    if api_key: req_url += '&apikey=' + api_key
    response = requests.get(req_url).json()
    if response.get('status'):
        if response.get('status') == '1':
            return int(response['result']) / 1000000000000000000
    return False
