from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def root_func():
    return redirect("https://www.mapua.edu.ph/")


if __name__ == '__main__':
    app.run(debug=True)
