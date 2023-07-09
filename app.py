from flask import Flask, request
from operations import *
app = Flask(__name__)




@app.route('/welcome')
def welcome_page():
    return "welcome"

@app.route('/welcome/home')
def welcome_home():
    return "welcome home"

@app.route('/welcome/back')
def welcome_back():
    return "welcome back"

# @app.route('/add')
# def add():
#     a = int(request.args.get("a"))
#     b = int(request.args.get("b"))
#     result = add(a, b)

#     return str(result)

# @app.route('/subtract')
# def subtract():
#     a = int(request.args.get("a"))
#     b = int(request.args.get("b"))
#     result = sub(a, b)

#     return str(result)

# @app.route('/multiply')
# def multiply():
#     a = int(request.args.get("a"))
#     b = int(request.args.get("b"))
#     result = mult(a, b)

#     return str(result)

# @app.route('/divide')
# def divide():
#     a = int(request.args.get("a"))
#     b = int(request.args.get("b"))
#     result = div(a, b)

#     return str(result)

operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
}

@app.route("/math/<oper>")
def math(oper):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)

    return str(result)
