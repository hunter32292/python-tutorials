import requests
import json
from pprint import pprint

def query_mockaroo(key):

    querystring = {"count":"1000","key":"18ef5990"}
    headers = {}

    response = requests.get(url='https://api.mockaroo.com/api/2a523c00',headers=headers,params=querystring)
    
    for value in json.loads(response.text):
        pprint(value)

if __name__ == "__main__":
    query_mockaroo('18ef5990')

