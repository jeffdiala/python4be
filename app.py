import logging
from helpers import http_code
from helpers.errors.GeneralError import GeneralError
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.errorhandler(GeneralError)
def generic_error_handler(ex):
    logging.error(ex.__str__())
    return jsonify({
        "message": ex.error,
        "detail": ex.details,
        "status": "error"
    }), http_code.HTTP_412_PRECONDITION_FAILED


@app.errorhandler(Exception)
def unhandled_exception(ex):
    logging.exception('Unhandled Exception: ' + ex.__str__())
    json502 = "{'error': '" + ex.__repr__() + "'}"
    return jsonify({
        "message": "Oh no There was an error",
        "detail": ex.__repr__(),
        "status": "error"
    }), http_code.HTTP_502_BAD_GATEWAY

@app.route("/user", methods=["POST"])
def user_func():
    # Make it so that input lname, fname are required
    data = request.get_json()

    try:
        lname = data.get("lname")
        fname = data.get("fname")
        if str(lname) == str(None):
            raise GeneralError(error="Missing required parameter",
                               details="Required parameter lname missing")

        if str(fname) == str(None):
            raise GeneralError(error="Missing required parameter",
                               details="Required parameter fname missing")

    except Exception as ex:
        logging.error(ex.__str__())
        if lname == None:
            param_missing = "lname"

        if fname == None:
            param_missing = "fname"

        raise GeneralError(error="Missing required parameter",
                           details="Required parameter {} missing".format(param_missing))
    return str(lname) + " " + str(fname)

if __name__ == '__main__':
    app.run(debug=True)
