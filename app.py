from flask import Flask

app = Flask(__name__)

@app.route("/")
def root_func():
    # how to make sure that a parameter from a body or a header is given to the endpoint?
    return "Test"


if __name__ == '__main__':
    app.run(debug=True)
