'''
:since: 13/08/2016
:author: oblivion
'''
from flask import Flask
from app.views import Add
from app.views import CustomerTable
from flask import g

# Init app and config
APP = Flask(__name__)
APP.config.from_object('config')
CONFIG = APP.config

@APP.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

APP.add_url_rule('/',
                 view_func=CustomerTable.as_view('table'),
                 methods=['GET'])
APP.add_url_rule('/add',
                 view_func=Add.as_view('add'),
                 methods=['GET', 'POST'])
