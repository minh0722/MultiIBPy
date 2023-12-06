from flask import Flask
from ib_insync import *

app = Flask(__name__)

@app.route("/")
def hello_world():
    response = "<p>Hello, World!</p>"
    return response

@app.route("/test")
def test():
    response = "<p>Hello, test!</p>"

    ib = IB()
    ib.connect('127.0.0.1', 7496, clientId=1, readonly=True)

    if(ib.isConnected):
        response += "<p>Connected!</p>"
        print("Connected!")

    return response