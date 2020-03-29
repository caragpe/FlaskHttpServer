import pytest
from app import app, db
from app.models import Banner


class TestSetBannerService:
    PIN = 3344
    INCORRECT_PIN = 3333
    BANNER_MESSAGE = "NewBannerHere"
    # Technically, 403 returns 'Forbidden'. Discuss specs!
    ERROR_403 = "METHOD NOT ALLOWED"
    ERROR_405 = "METHOD NOT ALLOWED"

    def test_auth_with_no_pin_in_header(self):
        with app.test_client() as c:
            rv = c.post('/set_banner?banner=' + self.BANNER_MESSAGE)
            assert rv.status_code == 403
            # assert 'FORBIDDEN' in rv.status
            assert self.ERROR_403 in rv.data.decode('utf-8')

    def test_auth_with_pin_in_header(self):
        with app.test_client() as c:
            rv = c.post('/set_banner?banner=' + self.BANNER_MESSAGE,
                        headers={'admin-auth': self.PIN}
                        )
            assert rv.status_code == 200
            assert rv.data.decode('utf-8') == ''

    def test_auth_with_incorrect_pin_in_header(self):
        with app.test_client() as c:
            rv = c.post('/set_banner?banner=' + self.BANNER_MESSAGE,
                        headers={'admin-auth': self.INCORRECT_PIN}
                        )
            assert rv.status_code == 403
            # assert 'FORBIDDEN' in rv.status
            assert self.ERROR_403 in rv.data.decode('utf-8')

    def test_wrong_auth_returns_method_not_allowed(self):
        with app.test_client() as c:
            rv = c.get('/set_banner?banner=' + self.BANNER_MESSAGE,
                       headers={'admin-auth': self.INCORRECT_PIN}
                       )
            assert rv.status_code == 405
            assert self.ERROR_405 in rv.status
        pass

    def test_valid_post_request_saves_to_db(self):
        with app.test_client() as c:
            rv = c.post('/set_banner?banner=' + self.BANNER_MESSAGE,
                        headers={'admin-auth': self.PIN}
                        )
            assert rv.status_code == 200
            assert rv.data.decode('utf-8') == ''
            last_banner_in_db = db.session \
                .query(Banner) \
                .order_by(Banner.id.desc()) \
                .first()
            assert last_banner_in_db.banner_message == self.BANNER_MESSAGE

        pass

    def test_banner_is_set_in_header_when_echoing(self):
        with app.test_client() as c:
            c.post('/set_banner?banner=' + self.BANNER_MESSAGE,
                   headers={'admin-auth': self.PIN}
                   )
            rv = c.get('/echo?message=JustASingleParam')
            assert rv.status_code == 200
            assert rv.data.decode('utf-8') == 'JustASingleParam'
            assert rv.headers['banner'] == self.BANNER_MESSAGE
        pass
