import pytest
from app import app


class TestEchoService:
    def test_single_param(self):
        with app.test_client() as c:
            rv = c.get('/echo?message=JustASingleParam')
            assert rv.status_code == 200
            assert rv.data.decode('utf-8') == 'JustASingleParam'

    def test_fails_message_empty_param_send(self):
        with app.test_client() as c:
            rv = c.get('/echo?message')
            assert rv.status_code == 406
            assert 'NOT ACCEPTABLE' in rv.status

    def test_fails_no_message_param_send(self):
        with app.test_client() as c:
            rv = c.get('/echo')
            assert rv.status_code == 406
            assert 'NOT ACCEPTABLE' in rv.status

    def test_fails_multiple_param_send(self):
        with app.test_client() as c:
            rv = c.get('/echo?message=Hello&from=Carlos')
            assert rv.status_code == 406
            assert 'NOT ACCEPTABLE' in rv.status

    def test_fails_when_http_method_distinct_from_get(self):
        with app.test_client() as c:
            rv = c.post('/echo?message=Hello')
            assert rv.status_code == 405
            assert 'METHOD NOT ALLOWED' in rv.status
