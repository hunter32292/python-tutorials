# from PACKAGE import CLASS
from flask import Flask, make_response, request
import json
import csv

app = Flask(__name__)

# Opens a file, takes that file,
# and puts contents into a payload var
def parseFile(filename):
    payload = ""
    for line in open(filename):
        payload = payload + line
    return payload

# Opens a file, takes that file,
# and puts contents into a payload var
def parseJsonFile(filename):
    dict_list = []
    # Read in CSV file with internal csv reader
    reader = csv.DictReader(open(filename))
    # Take Dictionary objects from CSV reader and add them to array
    for line in reader:
        dict_list.append(line)
    #  Using JSON dumps command, convert dictionary of values into JSON.
    return json.dumps(dict_list)

# localhost:8080/data
@app.route("/data")
def data():
    type_value = request.args.get('type')
    # Return CSV payload to consumer
    if type_value.lower().strip() == "csv":
        payload = parseFile("MOCK_DATA.csv")
        response = make_response(payload)
        response.headers["Content-Type"] = "text"
    # Return JSON payload to consumer
    elif type_value.lower().strip() == "json":
        payload = parseJsonFile("MOCK_DATA.csv")
        response = make_response(payload)
        response.headers["Content-Type"] = "application/json"
    # Return 404 to consumer
    else:
        response = make_response("Type Not Found", 404)

    return response

# localhost:8080/
@app.route("/")
def index():
    return "Hello World"

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)