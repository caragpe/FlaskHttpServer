from app import app, db
from flask import request, jsonify, Response
from app.errors import InvalidUsage
from app.infrastructure.banner_repository import BannerRepository
from app.services.echo_service import EchoService


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.route('/echo')
def echo():
    service = EchoService(request)
    result = service.echo()
    response = Response(result['message'])
    if result['last_banner'] is not None:
        response.headers['banner'] = result['last_banner']
    return response


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
