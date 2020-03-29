from flask import jsonify, Response
from app.infrastructure.banner_repository import BannerRepository
from app import app, db
from app.errors import InvalidUsage


class EchoService:
    ECHO_MESSAGE_PARAM = 'message'

    def __init__(self, request):
        self.request = request

    def echo(self):

        if self.request.method != 'GET':
            raise InvalidUsage('METHOD NOT ALLOWED', 405)
        string_params = dict(self.request.args)
        if len(string_params) != 1:
            raise InvalidUsage('NOT ACCEPTABLE', 406)
        message = self.request.args.get(self.ECHO_MESSAGE_PARAM)
        if message:
            repo = BannerRepository(db.session)
            last_banner = repo.get_last_banner_message()
            response = Response(message)
            if last_banner:
                response.headers['banner'] = last_banner
            return response
        else:
            raise InvalidUsage('NOT ACCEPTABLE', 406)

    @app.errorhandler(InvalidUsage)
    def handle_invalid_usage(self, error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response
