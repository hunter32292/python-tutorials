import requests
from pprint import pprint

def get():
    headers = {'accept': 'image/webp'}
    response = requests.get('https://httpbin.org/image', headers=headers)
    pprint(response)
    f = open("image.png", "wb")
    f.write(response.content)
    f.close()

if __name__ == "__main__":
    get()