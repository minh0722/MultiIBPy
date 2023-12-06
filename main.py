from flask import Flask
from ib_insync import *

app = Flask(__name__)

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1, readonly=True)

if(ib.isConnected):
    print("Connected!")

@app.route("/")
def hello_world():
    response = "<p>Hello, World!</p>"
    return response

@app.route("/test")
def test():
    response = "<p>Hello, test!</p>"

    return response

ib.disconnect()
print("Disconnected!")