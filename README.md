# README

## FlaskHttpServer

### Setting up the project

#### Creating a virtual environment

```
python3 -m venv venv
# Python3 is installed in /usr/local/bin/python3
virtualenv -p /usr/local/bin/python3 venv
# Activate it!
source venv/bin/activate
# To deactivate it, just type `deactivate`
```

#### Main dependencies
```shell script
pip install flask
pip install flask-sqlalchemy
pip install flask-migrate
pip install pytest
```

If you are using PyCharm, there is a `requiremets.txt` file that can be set up in `Tools > Python Integrated Tools > Packaging > Package requirements file` to automatically install these dependencies.

#### Export app name
```shell script
export FLASK_APP=server.py
```

#### Migrations
```shell script
flask db migrate -m "Message about this migration"
flask db upgrade
```

#### Running the server on 8081
```shell script
flask run -p 8081
```

#### Testing
To run the tests:
```shell script
python -m pytest tests/
```


Also, it can be run from each individual test file using PyCharm (`run 'pytest for test_{filename}`)
