# Working with Request Module and HTTP

Create a new directory or workspace called: **exercise-two**

`mkdir exercise-two`

### Requirements
Have installed:
- Postman

Pip install:
- requests
- pprint
- json

` pip install -MODULE NAME-`

### Creating a python script to work with REST endpoints

We'll be using [httpbin](https://httpbin.org/) a http mock service written in python flask


1. Create a Get call to `https://httpbin.org/get`

Create a file called `example.py`
```
import requests

def get():
    response = requests.get('https://httpbin.org/get')
    print(response)



if __name__ == "__main__":
    get()
```
From here you should see a status of `<Response [200]>` which means you suceeded the call

2. Cracking open the response object

Add to the exisiting function `get()` this will print out the internal 'attributes' of the response object
```
import requests
from pprint import pprint

def get():
    response = requests.get('https://httpbin.org/get')
    pprint(response.__dict__)

if __name__ == "__main__":
    get()
```
#### Example output from enhanced `get()`
```
{'_content': b'{\n  "args": {}, \n  "headers": {\n    "Accept": "*/*", \n    "A'
             b'ccept-Encoding": "gzip, deflate", \n    "Connection": "close"'
             b', \n    "Host": "httpbin.org", \n    "User-Agent": "python-req'
             b'uests/2.19.1"\n  }, \n  "origin": "98.99.245.37", \n  "url": "h'
             b'ttps://httpbin.org/get"\n}\n',
 '_content_consumed': True,
 '_next': None,
 'connection': <requests.adapters.HTTPAdapter object at 0x7fd95aabd518>,
 'cookies': <RequestsCookieJar[]>,
 'elapsed': datetime.timedelta(0, 0, 350969),
 'encoding': None,
 'headers': {'Connection': 'keep-alive', 'Server': 'gunicorn/19.9.0', 'Date': 'Mon, 22 Oct 2018 15:09:33 GMT', 'Content-Type': 'application/json', 'Content-Length': '266', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': 'true', 'Via': '1.1 vegur'},
 'history': [],
 'raw': <urllib3.response.HTTPResponse object at 0x7fd95aacc2b0>,
 'reason': 'OK',
 'request': <PreparedRequest [GET]>,
 'status_code': 200,
 'url': 'https://httpbin.org/get'}
 ```
This should show you exactly what is use in the reponse body of a request object

3. Handle a bad responses and different HTTP protocol responses

Please go to `https://httpstatusdogs.com/` and start to review some of the response codes you'll see, specficially look at 1XX,2XX,3XX,4XX,5XX response codes and understand the differences. Once you have an idea of what those look like, lets try hitting a bad enpoint `https://httpstat.us/` has a number of endpoint that have 'bad' response codes.

```
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

```

4. Handling JSON payload and URL queries

Use your internet browser to navigate to `https://www.mockaroo.com/api/docs` where we can start working with API data (You will need to login, or borrow a API key for Mockaroo today)

```
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

```

5. Handling something other than JSON

For this last example, we'll work with the binary data from a response content and dump that information out to a file where we can work with it.

```
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
```
