# FlaskHttpServer

## Setting up the project

### Creating a virtual environment

```
python3 -m venv venv
# Python3 is installed in /usr/local/bin/python3
virtualenv -p /usr/local/bin/python3 venv
# Activate it!
source venv/bin/activate
# To deactivate it, just type `deactivate`
```

### Main dependencies
```shell script
pip install flask
pip install flask-sqlalchemy
pip install flask-migrate
pip install pytest
```

If you are using PyCharm, there is a `requiremets.txt` file that can be set up in `Tools > Python Integrated Tools > Packaging > Package requirements file` to automatically install these dependencies.

### Export app name
```shell script
export FLASK_APP=server.py
```

### Migrations
```shell script
flask db migrate -m "Message about this migration"
flask db upgrade
```

### Running the server on 8081
```shell script
flask run -p 8081
```

### Testing
To run the tests:
```shell script
python -m pytest tests/
```

Also, it can be run from each individual test file using PyCharm (`run 'pytest for test_{filename}`)

### Usage
Open two terminals. On the first one, start the server as described before. On the second one, submit GET and POST requests:
```shell script
# GET request
curl -v -X GET http://127.0.0.1:8081/echo?message={message_here}
# POST request
curl -v -X POST -H "admin-auth: 3344" http://127.0.0.1:8081/set_banner?banner={header_banner_here}
```

#### Echo endpoint
The `/echo` endpoint accepts exclusively `GET` requests and accepts a single parameter `message`.
- If no message is passed or any additional parameter is given, it should return:
`406 NOT ACCEPTABLE`.
- If a wrong request type is sent, it should respond with `405 METHOD NOT
ALLOWED`
- If the request is fine, the response should contain the message passed in the
request.

#### SetBanner endpoint
The `/setbanner` endpoint should accept a `POST` request with a single parameter `banner` in the `POST` body.
- The request should be authenticated with a PIN code set in the headers. The correct pin is 3344 and header name is `admin-auth`
- If authentication fails it should return: `403 METHOD NOT ALLOWED`
- If the request is right, response should be empty.
- After a correct setting, banner should be returned in the header in all further
responses to the `/echo` endpoint.