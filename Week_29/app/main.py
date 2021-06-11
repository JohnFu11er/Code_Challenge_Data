import requests
from fastapi import FastAPI
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


app = FastAPI()

@app.get("/easy")
def easy():
    ''' Returns the name of the current dunder name variable '''
    return {
        "message" : f'special variable __name__ is currently set to: {__name__}'
    }
    
@app.get("/medium/{username}/{password}")
def medium(username: str, password: str):
    ''' Returns the API authorization key from Cisco Devnet '''
    return basic_auth(username, password)

@app.get("/hard/{username}/{password}")
def hard(username: str, password: str):
    ''' Returns following data for each device:
    - Device Name
    - Device Type
    - Last Updated
    '''
    
    devices = device_list(username, password)

    output = {}

    for dev in devices['response']:
        output[dev['hostname']] = {
                "Device Name" : dev['hostname'],
                "Device Type" : dev['series'],
                "Last Updated" : dev['lastUpdated']
            }
        
    return output