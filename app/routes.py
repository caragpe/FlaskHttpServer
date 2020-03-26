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
    ECHO_MESSAGE_PARAM = 'message'
    if request.method != 'GET':
        raise InvalidUsage('METHOD NOT ALLOWED', 405)
    string_params = dict(request.args)
    if len(string_params) != 1:
        raise InvalidUsage('NOT ACCEPTABLE', 406)
    content_param = request.args.get(ECHO_MESSAGE_PARAM)
    if content_param:
        return content_param
    else:
        raise InvalidUsage('NOT ACCEPTABLE', 406)


@app.route('/set_banner', methods=['POST'])
def set_banner():
    if request.method != 'POST':
        raise InvalidUsage('METHOD NOT ALLOWED', 405)
    pass
