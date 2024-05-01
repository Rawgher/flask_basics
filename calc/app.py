import operations
from flask import Flask, request

app = Flask(__name__)

@app.route("/add")
def add():
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = operations.add(a,b)
    return str(result)

@app.route("/sub")
def subtract():
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = operations.sub(a,b)
    return str(result)

@app.route("/mult")
def multiply():
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = operations.mult(a,b)
    return str(result)

@app.route("/div")
def divide():
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = operations.div(a,b)
    return str(result)