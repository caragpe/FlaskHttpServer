import pytest
from app import app


class TestSetBannerService:
    PIN = 3344
    INCORRECT_PIN = 3333

    def test_auth_with_no_pin_in_header(self):
        with app.test_client() as c:
            rv = c.post('/set_banner?banner=NewBanner')
            assert rv.status_code == 403
            # assert 'FORBIDDEN' in rv.status
            assert 'METHOD NOT ALLOWED' in rv.data.decode('utf-8')

    def test_auth_with_pin_in_header(self):
        with app.test_client() as c:
            rv = c.post('/set_banner?banner=NewBanner',
                        headers={'admin-auth': self.PIN}
                        )
            assert rv.status_code == 200
            assert rv.data.decode('utf-8') == ''

    def test_auth_with_incorrect_pin_in_header(self):
        with app.test_client() as c:
            rv = c.post('/set_banner?banner=NewBanner',
                        headers={'admin-auth': self.INCORRECT_PIN}
                        )
            assert rv.status_code == 403
            # assert 'FORBIDDEN' in rv.status
            assert 'METHOD NOT ALLOWED' in rv.data.decode('utf-8')

    def test_wrong_auth_returns_method_not_allowed(self):
        with app.test_client() as c:
            rv = c.get('/set_banner?banner=NewBanner',
                       headers={'admin-auth': self.INCORRECT_PIN}
                       )
            assert rv.status_code == 405
            assert 'METHOD NOT ALLOWED' in rv.status
        pass

    def test_valid_post_request(self):
        pass

    def test_banner_is_set_in_header_when_echoing(self):
        pass
