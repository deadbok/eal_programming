#!/usr/bin/python
'''
:since: 01/08/2015
:author: oblivion
'''
from app import APP

APP.run(debug=APP.config['DEBUG'], host='0.0.0.0')
