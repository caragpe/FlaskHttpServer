import pytest
from server import app


class TestEcho:
    def test_basic_echo(self):
        with app.test_client() as c:
            rv = c.get('/echo?message=Hello')
            assert rv.status_code == 200
            assert rv.data == b'Hello'

    def test_fails_no_message_param_send(self):
        with app.test_client() as c:
            rv = c.get('/echo')
            assert rv.status_code == 406
            assert b'NOT ACCEPTABLE' in rv.data

    def test_fails_multiple_param_send(self):
        with app.test_client() as c:
            rv = c.get('/echo?message=Hello&from=Carlos')
            assert rv.status_code == 406
            assert b'NOT ACCEPTABLE' in rv.data

    def test_fails_when_http_method_distinct_from_get(self):
        with app.test_client() as c:
            rv = c.post('/echo?message=Hello&from=Carlos')
            assert rv.status_code == 405
            # assert b'Method not allowed' in rv.data
