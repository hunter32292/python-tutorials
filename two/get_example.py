import requests
from pprint import pprint

def get():
    response = requests.get('https://httpbin.org/get')
    pprint(response.__dict__)

if __name__ == "__main__":
    get()