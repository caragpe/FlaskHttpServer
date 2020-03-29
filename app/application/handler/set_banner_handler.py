from app.infrastructure.banner_repository import BannerRepository
from app import db
from app.errors import InvalidUsage


class SetBannerHandler:
    SET_BANNER_PARAM = 'banner'

    def __init__(self, request):
        self.method = request.method
        self.headers = request.headers
        self.args_inbound = request.args

    def set_banner(self):
        self.validate_set_banner_request()
        new_banner = self.args_inbound.get(self.SET_BANNER_PARAM)
        if new_banner:
            repo = BannerRepository(db.session)
            result = repo.save_banner_message(new_banner)
            return result
        else:
            raise InvalidUsage('NOT ACCEPTABLE', 406)

    def validate_set_banner_request(self):
        if self.method != 'POST':
            raise InvalidUsage('METHOD NOT ALLOWED', 405)
        if "admin-auth" not in self.headers:
            # Review if should be Forbidden
            raise InvalidUsage('METHOD NOT ALLOWED', 403)
        if self.headers['admin-auth'] != '3344':
            # Review if should be Forbidden
            raise InvalidUsage('METHOD NOT ALLOWED', 403)
        if len(self.args_inbound) != 1:
            raise InvalidUsage('NOT ACCEPTABLE', 406)
