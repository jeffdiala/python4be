from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def root_func():
    return "Hello World"


@app.route("/from/headers")
def get_from_headers():
    pass

@app.route("/from/query")
def get_from_query_params():
    pass

@app.route("/from/url/<in_value>")
def get_from_url(in_value):
    pass

@app.route("/from/body")
def get_from_json():
    pass

if __name__ == '__main__':
    app.run(debug=True)
