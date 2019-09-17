from flask import Flask, make_response, request
import json
import csv

app = Flask(__name__)

def parseDatafile(filename):
    payload = ""
    for line in open(filename):
        payload += line
    return payload

def parseJsonDatafile(filename):
    dict_list = []
    # Read in CSV file with internal csv reader
    reader = csv.DictReader(open(filename))
    # Take Dictionary objects from CSV reader and add them to array
    for line in reader:
        dict_list.append(line)
    #  Using JSON dumps command, convert dictionary of values into JSON.
    return json.dumps(dict_list)

@app.route('/data')
def data():
    responseType = request.args.get('type')

    if responseType == "json":
        payload = parseJsonDatafile("MOCK_DATA.csv")
        response = make_response(payload)
        response.headers["Content-type"] = "application/json"
    elif responseType == "csv":
        payload = parseDatafile("MOCK_DATA.csv")
        response = make_response(payload)
        response.headers["Content-type"] = "text"
    else:
        response = make_response("Type Not Found", 404)
    
    return response

@app.route('/')
def index():
    return "Hello, World"

if __name__ == "__main__":
    app.run(host="localhost", port="8080", debug=True)