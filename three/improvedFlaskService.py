from flask import Flask, make_response

app = Flask(__name__)


def parseFile(filename):
    payload = ""
    for line in open(filename):
        payload = payload + line
    return payload

@app.route("/data")
def data():
    payload = parseFile("MOCK_DATA.csv")
    response = make_response(payload)
    response.headers["Content-type"] = "text"
    return response

@app.route('/')
def index():
    return "Hello, World"

if __name__ == "__main__":
    app.run(host="localhost", port="8080", debug=True)