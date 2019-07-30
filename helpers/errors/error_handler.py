import logging
from flask import jsonify
from helpers.errors.GeneralError import GeneralError
from helpers import http_code

def register_errors(app):
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
        json502 = "{'error': '" + ex.__str__() + "'}"
        return jsonify({
            "message": "Oh no There was an error",
            "detail": ex.__str__(),
            "status": "error"
        }), http_code.HTTP_502_BAD_GATEWAY
