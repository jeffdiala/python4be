from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def root_func():
    return "Hello World"


@app.route("/from/headers")
def get_from_headers():
    token = request.headers.get("token")

    return token


@app.route("/from/query")
def get_from_query_params():
    lname = request.args.get("lname")
    fname = request.args.get("fname")

    return fname + " " + lname


@app.route("/from/url/<in_value>")
def get_from_url(in_value):
    return in_value

@app.route("/from/body")
def get_from_json():
    data = request.get_json()

    return str(data["fname"]) + " " + str(data["lname"])


if __name__ == '__main__':
    app.run(debug=True)
