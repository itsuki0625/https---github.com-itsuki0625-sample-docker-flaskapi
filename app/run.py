"""app/run.py"""
import os

from flask import Flask
from flask_migrate import Migrate

from app.v1.views.main import v1
from app.v1.models import db
from app.v1.common.utility import err_response

app = Flask(__name__)
app.config.from_pyfile('config.py')
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(v1)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/about', methods=['GET'])
def about():
    return "about page"

@app.errorhandler(404)
@app.errorhandler(500)
def errorhandler(error):
    """errorhandler
    """
    return err_response(error=error), error.code

def main():
    """main
    """
    host = '0.0.0.0'
    port = 5555

    app.run(host=host, port=port)


if __name__ == '__main__':
    main()