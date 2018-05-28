#! /usr/bin/python3

import requests
import json

baseURL = 'https://mhw-db.com/'

def get(path, param = None):
    """GET from path"""

    if param:
        response = requests.get(baseURL + path + '/' + str(param))
    else:
        response = requests.get(baseURL + path)
    
    response.raise_for_status()

    res = json.loads(response.text)
    return json.dumps(res, indent = 2)

def getValue(response, key):
    """Snip values of given key from a GET response"""

    r = json.loads(response)
    keyVal = r[key]
    val = json.dumps(keyVal, indent = 2)

    return val

if __name__ == "__main__":

    param = 'dodogama-mail'
    resp = get('armour', param)
    name = getValue(resp, 'name')
    img = getValue(resp, 'assets')

    print('Response: %s\n%s' % (name, img))
