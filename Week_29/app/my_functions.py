import json
import requests
from requests.auth import HTTPBasicAuth

def basic_auth(username, password):    

    api_URL = 'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token'

    data = requests.post(
        api_URL,
        auth=HTTPBasicAuth(username, password)
    ).json()

    return data


def device_list(username, password):
    api_auth = basic_auth(username, password)
    
    headers = {
    'X-Auth-Token': api_auth['Token'],
    'content-type': 'application/json'
    }

    api_URL = "http://sandboxdnac.cisco.com/dna/intent/api/v1/network-device"
    data = requests.get(
        api_URL,
        headers= headers
    ).json()
    
    return data