# Working with Flask Services

Create a new directory or workspace called: **exercise-three**

For anyone looking for the order of change in the files included:
- flaskService.py
- improvedFlaskService.py
- moreImprovedFlaskService.py
- veryimprovedFlaskService.py
- fullFlaskService.py *This has a large number of comments to explain the code*


`mkdir exercise-three`

### Requirements
Have installed:
- Postman

Pip install:
- flask

#### Do this at the start:
- `python3 -m venv venv`
- `source venv/bin/activate`
- `pip3 install -MODULE NAME-`

### Creating a simple flask service, to share data


# 1. Create a basic dataset from https://mockaroo.com/ for our flask API

The new dataset should have the following fields:

- id
- first_name
- last_name
- email
- gender
- ip_address

```
id,first_name,last_name,email,gender,ip_address
1,Rosella,Brownrigg,rbrownrigg0@about.com,Female,220.247.56.234
```

Save the file as `MOCK_DATA.csv` in your directory


# 2. Create a basic python flask service
Create a new virtual environment `python3 -m venv venv`
Install Flask `pip3 install flask`
Create a file called `flaskService.py`

```
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World"

if __name__ == "__main__":
    app.run(host="localhost", port="8080", debug=True)
```

#### **Head to the browser**
[http://localhost:8080](http://localhost:8080)

You should see a simple 'hello world'

# 3. Add a data endpoint to our simple flask API

Add an additional endpoint, that will parse our data file and hand back the information via the new endpoint.
It should open the file and create a flask `Response` object for the endpoint.

```
from flask import Flask, make_response
import json

app = Flask(__name__)


def parseDatafile(filename):
    payload = ""
    for line in open(filename):
        payload += line

    return payload


@app.route('/data')
def data():
    payload = parseDatafile("MOCK_DATA.csv")
    response = make_response(payload)
    response.headers["Content-type"] = "text"

    return response

@app.route('/')
def index():
    return "Hello, World"

if __name__ == "__main__":
    app.run(host="localhost", port="8080", debug=True)

```

# 4. Provide the data as either a CSV or JSON, based on a query param passed to the data endpoint

Add an option to return both a CSV and a JSON data payload for anyone that is looking at the `/data` endpoint based on a query param of `?type=csv` or `?type=json` it should not worry about casing or spaces

ex: `localhost:8080/data?type=json`

```
from flask import Flask, make_response, request
import json
import csv

app = Flask(__name__)


def parseDatafile(filename):
    payload = ""
    for line in open(filename):
        payload += line

    return payload

def parseDatafileToJson(filename):
    dict_list = []
    reader = csv.DictReader(open(filename))
    for line in reader:
        dict_list.append(line)
    return json.dumps(dict_list)


@app.route('/data')
def data():
    responseType = request.args.get('type')
    if "json" == responseType.strip().lower():
        payload = parseDatafileToJson("MOCK_DATA.csv")
        response = make_response(payload)
        response.headers["Content-type"] = "application/json"
    elif "csv" == responseType.strip().lower():
        payload = parseDatafile("MOCK_DATA.csv")
        response = make_response(payload)
        response.headers["Content-type"] = "text"
    else:
        payload = "Response Type Not Found ..."
        response = make_response(payload, 404)
        response.headers["Content-type"] = "text"

    return response

@app.route('/')
def index():
    return "Hello, World"

if __name__ == "__main__":
    app.run(host="localhost", port="8080", debug=True)

```

# 5. Use a Dict to store in memory the data that is provided via the data endpoints

Using a Dict object, create an in memory cache for your session. This cache should contain the current requests you've made for a dataset on the `/data` endpoint and return data without needing to parse it out into a response.

```
from flask import Flask, make_response, request
import json
import csv

session = {}
app = Flask(__name__)

def parseDatafile(filename):
    payload = ""
    for line in open(filename):
        payload += line

    return payload

def parseDatafileToJson(filename):
    dict_list = []
    reader = csv.DictReader(open(filename))
    for line in reader:
        dict_list.append(line)
    return json.dumps(dict_list)


@app.route('/data')
def data():
    responseType = request.args.get('type')
    if "json" == responseType.strip().lower():
        if "json" in session.keys():
            print("Found in memory ...")
            return session["json"]
        payload = parseDatafileToJson("MOCK_DATA.csv")
        response = make_response(payload)
        response.headers["Content-type"] = "application/json"
        
        session["json"] = response
    elif "csv" == responseType.strip().lower():
        if "csv" in session.keys():
            print("Found in memory ...")
            return session["csv"]
        payload = parseDatafile("MOCK_DATA.csv")
        response = make_response(payload)
        response.headers["Content-type"] = "text/csv"
        session["csv"] = session
    else:
        payload = "Response Type Not Found ..."
        response = make_response(payload, 404)
        response.headers["Content-type"] = "text"
    return response

@app.route('/')
def index():
    return "Hello, World"

if __name__ == "__main__":
    app.run(host="localhost", port="8080", debug=True)
```
