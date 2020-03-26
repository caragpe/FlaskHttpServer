# README

## FlaskHttpServer

### Setting up the project

#### Creating a virtual environment

Virtual Env
```
python3 -m venv venv
# Python3 is installed in /usr/local/bin/python3
virtualenv -p /usr/local/bin/python3 venv
# Activate it!
source venv/bin/activate
# To deactivate it, just type `deactivate`
```

Main dependencies
```shell script
pip install flask
pip install flask-sqlalchemy
pip install flask-migrate
```

```shell script
export FLASK_APP=set_banner_service.py
```

Migrations
```shell script
flask db migrate -m "Message about this migration"
flask db upgrade
```

Running the server on 8081
```shell script
flask run -p 8081
```