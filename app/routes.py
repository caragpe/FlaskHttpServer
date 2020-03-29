from app import app, db
from flask import request, jsonify, Response
from app.errors import InvalidUsage
from app.infrastructure.banner_repository import BannerRepository
from app.services import echo_service


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.route('/echo')
def echo():
    service = echo_service.EchoService(request)
    result = service.echo()
    return result

    # ECHO_MESSAGE_PARAM = 'message'
    # if request.method != 'GET':
    #     raise InvalidUsage('METHOD NOT ALLOWED', 405)
    # string_params = dict(request.args)
    # if len(string_params) != 1:
    #     raise InvalidUsage('NOT ACCEPTABLE', 406)
    # message = request.args.get(ECHO_MESSAGE_PARAM)
    # if message:
    #     repo = BannerRepository(db.session)
    #     last_banner = repo.get_last_banner_message()
    #     response = Response(message)
    #     if last_banner:
    #         response.headers['banner'] = last_banner
    #     return response
    # else:
    #     raise InvalidUsage('NOT ACCEPTABLE', 406)


@app.route('/set_banner', methods=['POST'])
def set_banner():
    SET_BANNER_PARAM = 'banner'
    if request.method != 'POST':
        raise InvalidUsage('METHOD NOT ALLOWED', 405)
    headers = request.headers
    if "admin-auth" not in headers:
        # Review if should be Forbidden
        raise InvalidUsage('METHOD NOT ALLOWED', 403)
    if headers['admin-auth'] != '3344':
        # Review if should be Forbidden
        raise InvalidUsage('METHOD NOT ALLOWED', 403)
    string_params = dict(request.args)
    if len(string_params) != 1:
        raise InvalidUsage('NOT ACCEPTABLE', 406)
    new_banner = request.args.get(SET_BANNER_PARAM)
    if new_banner:
        repo = BannerRepository(db.session)
        result = repo.save_banner_message(new_banner)
        if result is not None:
            return Response(status=200)
        else:
            return Response(status=500)
    else:
        raise InvalidUsage('NOT ACCEPTABLE', 406)
