# -*- coding: utf-8 -*-
"""
Name: Main initialisation of the Flask program.
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0.0 (2017-04-30)
"""
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
    """
    Function to close the database connaction when the current session closes. 
    """
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Add the / view.
APP.add_url_rule('/',
                 view_func=CustomerTable.as_view('table'),
                 methods=['GET'])
# Add the /add view.
APP.add_url_rule('/add',
                 view_func=Add.as_view('add'),
                 methods=['GET', 'POST'])
