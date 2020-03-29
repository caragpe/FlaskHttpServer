from app import app, db
from flask import request, jsonify, Response
from app.errors import InvalidUsage
from app.application.services.echo_service import EchoService
from app.application.handler.set_banner_handler import SetBannerHandler


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
    handler = SetBannerHandler(request)
    result = handler.set_banner()
    if result is not None:
        return Response(status=200)
    else:
        return Response(status=500)
