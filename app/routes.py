from app import app
from flask import request, jsonify
from app.errors import InvalidUsage


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.route('/echo')
def echo():
    if request.method != 'GET':
        raise InvalidUsage('METHOD NOT ALLOWED', 405)
    pass


@app.route('/set_banner', methods=['POST'])
def set_banner():
    if request.method != 'POST':
        raise InvalidUsage('METHOD NOT ALLOWED', 405)
    pass
