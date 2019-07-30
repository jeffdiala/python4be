from flask import Flask

app = Flask(__name__)

@app.route("/")
def root_func():
    # Returning a string will give status 200
    return "Test"

    # try returning a different Status
    # try returning a tuple
    # try returning a list
    # try returning a dictionary


if __name__ == '__main__':
    app.run(debug=True)
