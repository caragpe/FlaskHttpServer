from flask import jsonify
from app.infrastructure.banner_repository import BannerRepository
from app import app, db
from app.errors import InvalidUsage


class EchoService:
    ECHO_MESSAGE_PARAM = 'message'

    def __init__(self, request):
        self.request = request

    def echo(self):
        self.validate_echo_request()
        message = self.request.args.get(self.ECHO_MESSAGE_PARAM)
        if message:
            repo = BannerRepository(db.session)
            last_banner = repo.get_last_banner_message()
            return {'message': message, 'last_banner': last_banner}
        else:
            raise InvalidUsage('NOT ACCEPTABLE', 406)

    def validate_echo_request(self):
        if self.request.method != 'GET':
            raise InvalidUsage('METHOD NOT ALLOWED', 405)
        string_params = dict(self.request.args)
        if len(string_params) != 1:
            raise InvalidUsage('NOT ACCEPTABLE', 406)


    @app.errorhandler(InvalidUsage)
    def handle_invalid_usage(self, error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response
