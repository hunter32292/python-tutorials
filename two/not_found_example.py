import requests
from pprint import pprint

def get():
    response = requests.get('https://httpbin.org/status/404')
    pprint(response.__dict__)

if __name__ == "__main__":
    get()