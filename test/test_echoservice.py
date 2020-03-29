import pytest
from app import app


class TestEchoService:
    MESSAGE = "JustASingleParam"
    ERROR_406 = "NOT ACCEPTABLE"
    ERROR_405 = "METHOD NOT ALLOWED"

    def test_single_param(self):
        with app.test_client() as c:
            rv = c.get('/echo?message=' + self.MESSAGE)
            assert rv.status_code == 200
            assert rv.data.decode('utf-8') == self.MESSAGE

    def test_fails_message_empty_param_send(self):
        with app.test_client() as c:
            rv = c.get('/echo?message')
            assert rv.status_code == 406
            assert self.ERROR_406 in rv.status

    def test_fails_no_message_param_send(self):
        with app.test_client() as c:
            rv = c.get('/echo')
            assert rv.status_code == 406
            assert self.ERROR_406 in rv.status

    def test_fails_multiple_param_send(self):
        with app.test_client() as c:
            rv = c.get('/echo?message=' + self.MESSAGE + '&message2=Other')
            assert rv.status_code == 406
            assert self.ERROR_406 in rv.status

    def test_fails_when_http_method_distinct_from_get(self):
        with app.test_client() as c:
            rv = c.post('/echo?message=' + self.MESSAGE)
            assert rv.status_code == 405
            assert self.ERROR_405 in rv.status
