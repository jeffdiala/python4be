import http
from flask import Flask, jsonify, request
from helpers.EmployeeDB_Util import EmployeeDB_Util
from helpers.errors.error_handler import register_errors

app = Flask(__name__)

register_errors(app)


@app.route("/", methods=["GET"])
def default_func():
    return jsonify({
        'status': 'OK',
        'version': '0.0.1',
        'environment': 'development'
    }), http.HTTPStatus.OK


@app.route("/user", methods=["POST"])
def user_func():
    # Make it so that input lname, fname are required
    data = request.get_json()

    employee_util = EmployeeDB_Util("employees.csv")
    fname = data.get("fname")
    employee_list = employee_util.searchEmployee(fname)
    response = {"search_result": employee_list}

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
