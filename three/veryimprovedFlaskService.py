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