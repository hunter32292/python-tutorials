import requests
from pprint import pprint

def moved_request():
    response = requests.get('https://httpstat.us/301')
    pprint(response.__dict__)

def bad_request():
    response = requests.get('https://httpstat.us/400')
    pprint(response.__dict__)

def server_error_request():
    response = requests.get('https://httpstat.us/500')
    pprint(response.__dict__)        

if __name__ == "__main__":
    moved_request()
    bad_request()
    server_error_request()