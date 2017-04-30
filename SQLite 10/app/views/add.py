# -*- coding: utf-8 -*-
"""
Name: Add customer view.
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0.0 (2017-04-30)
"""
from flask import render_template, url_for, redirect, request
from flask.views import MethodView

from app.models import CustomerDB


class Add(MethodView):
    '''
    View to add a customer
    '''
    # Only support GET and POST requests to get data from the form.
    methods = ['GET', 'POST']

    def get(self):
        '''
        Render the add viewn.
        '''
        # Render the template for the customer table.
        return render_template('add.html')

    def post(self):
        '''
        Handle submission of a new customer.
        '''
        print(str(request.form['name']))
        name = request.form['name']
        email = request.form['email']
        address = request.form['address']
        city = request.form['city']
        CustomerDB().add(name, email, address, city)

        # Redirect to the customer table.
        return redirect(url_for('table'))