from fastapi import FastAPI
from my_functions import basic_auth, device_list

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