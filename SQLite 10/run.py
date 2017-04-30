#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Name: Main program to run the debug version of the Flask application.
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0.0 (2017-04-30)
"""
from app import APP

# Run the Flask application in debug mode.
APP.run(debug=APP.config['DEBUG'], host='0.0.0.0')
